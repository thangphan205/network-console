import requests
from nornir.core.task import Task
from settings import settings


def netmiko_handler(task: Task, fast_cli: bool) -> None:
    """
    The purpose of this handler is two folds:
        + Make sure netmiko uses the correct `fast_cli` setting for each function.
        + Work around for the error `search pattern never detected` on Aruba switches
          by calling the `find_prompt()` method to return the trailing prompt.
    """
    if "netmiko" in task.host.connections:
        if task.host.connections["netmiko"].connection.is_alive():
            if (
                task.host.platform == "ios"
                and task.host.connections["netmiko"].connection.fast_cli != fast_cli
            ):
                task.host.close_connection("netmiko")

            elif task.host.platform == "hp_procurve":
                task.host.connections["netmiko"].connection.find_prompt()
        else:
            task.host.close_connection("netmiko")


def http_handler(
    task: Task, url: str, plugin: str, method: str = "get", **kwargs
) -> requests.models.Response:
    """TLS_VERIFYll. If failed, it will then try to establish
    a new connection to the device.

    Args:
        task: a Task object.
        url: the url to query.
        plugin: the plugin used to setup connection to the device.
        method: the HTTP method to perform on the device.
        **kwargs: keyword arguments to be passed to request

    Returns:
        A Response object.

    Raises:
        ValueError: for error status code.
    """
    headers = task.host.get_connection(
        plugin, task.nornir.config
    )  # reuse the previous cookie
    rsp = requests.request(
        method, url, headers=headers, verify=settings.TLS_VERIFY, timeout=5, **kwargs
    )
    if rsp.status_code != 200 and rsp.status_code != 201:
        if "session timed out" in rsp.text:
            task.host.connections[plugin].session_timed_out = True
            task.host.close_connection(plugin)
            headers = task.host.get_connection(
                plugin, task.nornir.config
            )  # establish new connection
            rsp = requests.request(
                method,
                url,
                headers=headers,
                verify=settings.TLS_VERIFY,
                timeout=5,
                **kwargs,
            )
            if rsp.status_code != 200 and rsp.status_code != 201:
                raise ValueError(f"{rsp.status_code} {rsp.reason}: {rsp.text}.")
        else:
            raise ValueError(f"{rsp.status_code} {rsp.reason}: {rsp.text}.")
    return rsp
