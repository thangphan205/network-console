import request from '@/utils/request';

export async function query(): Promise<any> {
  return request('/api/users');
}
export async function queryCurrent(): Promise<any> {
  const token = localStorage.getItem("access_token");
  const bearer = 'Bearer ' + token;
  const response = request('/api/users/currentUser', {
    headers: {
      'Authorization': bearer,
    }
  });
  return response;
}
export async function queryNotices(): Promise<any> {
  return request('/api/notices');
}

