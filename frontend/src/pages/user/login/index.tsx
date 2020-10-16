import { Alert, Card, Checkbox } from 'antd';
import React, { useState } from 'react';
import { Link, connect, Dispatch } from 'umi';
import { StateType } from '@/models/login';
import { LoginParamsType } from '@/services/login';
import { ConnectState } from '@/models/connect';
import LoginForm from './components/Login';

import styles from './style.less';

const { Tab, UserName, Password, Submit } = LoginForm;
interface LoginProps {
  dispatch: Dispatch;
  userLogin: StateType;
  submitting?: boolean;
}

const LoginMessage: React.FC<{
  content: string;
}> = ({ content }) => (
  <Alert
    style={{
      marginBottom: 24,
    }}
    message={content}
    type="error"
    showIcon
  />
);

const Login: React.FC<LoginProps> = (props) => {
  const { userLogin = {}, submitting } = props;
  const { status, type: loginType } = userLogin;
  const [autoLogin, setAutoLogin] = useState(true);
  const [type, setType] = useState<string>('account');

  const handleSubmit = (values: LoginParamsType) => {
    const { dispatch } = props;
    dispatch({
      type: 'login/login',
      payload: { ...values, type },
    });
  };
  return (
    <div className={styles.main}>
      <LoginForm activeKey={type} onTabChange={setType} onSubmit={handleSubmit}>
        <Tab key="account" tab="Account">
          {status === 'error' && loginType === 'account' && !submitting && (
            <LoginMessage content="Demo account（admin/hocmang.net）" />
          )}

          <UserName
            name="userName"
            placeholder="Username: admin or user"
            rules={[
              {
                required: true,
                message: 'Please enter username!',
              },
            ]}
          />
          <Password
            name="password"
            placeholder="Password: hocmang.net"
            rules={[
              {
                required: true,
                message: 'Please enter password！',
              },
            ]}
          />
        </Tab>

        {/* <div>
          <Checkbox checked={autoLogin} onChange={(e) => setAutoLogin(e.target.checked)}>
            Remember me
          </Checkbox>
          <a
            style={{
              float: 'right',
            }}
          >
            Forgot
          </a>
        </div> */}
        <Submit loading={submitting}>Login</Submit>
      </LoginForm>

    </div>
  );
};

export default connect(({ login, loading }: ConnectState) => ({
  userLogin: login,
  submitting: loading.effects['login/login'],
}))(Login);
