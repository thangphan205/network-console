import request from '@/utils/request';

export interface LoginParamsType {
  userName: string;
  password: string;
  mobile: string;
  captcha: string;
}

export async function getFakeCaptcha(mobile: string) {
  return request(`/api/login/captcha?mobile=${mobile}`);
}

export async function fakeAccountLogin(params: LoginParamsType) {
  const login_params = "username=" + params.userName + "&password=" + params.password;
  return request('/api/login/account', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    data: login_params,
  });
}