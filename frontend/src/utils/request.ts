/**
 * request 网络请求工具
 * 更详细的 api 文档: https://github.com/umijs/umi-request
 */
import { extend } from 'umi-request';
import { notification } from 'antd';

const codeMessage = {
  200: 'Response code 200',
  201: 'Response code 201',
  202: 'Response code 202',
  204: 'Response code 204',
  400: 'Response code 400',
  401: 'Response code 401',
  403: 'Response code 403',
  404: 'Response code 404',
  406: 'Response code 406',
  410: 'Response code 410',
  422: 'Response code 422',
  500: 'Response code 500',
  502: 'Response code 502',
  503: 'Response code 503',
  504: 'Response code 504',
};

/**
 * 异常处理程序
 */
const errorHandler = (error: { response: Response }): Response => {
  const { response } = error;
  if (response && response.status) {
    const errorText = codeMessage[response.status] || response.statusText;
    const { status, url } = response;

    notification.error({
      message: `Error ${status}: ${url}`,
      description: errorText,
    });
  } else if (!response) {
    notification.error({
      description: 'Cannot connect to server.',
      message: 'Network issue.',
    });
  }
  return response;
};

/**
 * 配置request请求时的默认参数
 */
const request = extend({
  errorHandler, // 默认错误处理
  credentials: 'include', // 默认请求是否带上cookie
});

export default request;
