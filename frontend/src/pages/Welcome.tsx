import React from 'react';
import { PageContainer } from '@ant-design/pro-layout';
import { Card, Alert, Typography } from 'antd';
import styles from './Welcome.less';

const CodePreview: React.FC<{}> = ({ children }) => (
  <pre className={styles.pre}>
    <code>
      <Typography.Text copyable>{children}</Typography.Text>
    </code>
  </pre>
);

export default (): React.ReactNode => (
  <PageContainer>
    <Card>
      <Alert
        message="ok"
        type="success"
        showIcon
        banner
        style={{
          margin: -12,
          marginBottom: 24,
        }}
      />
      <Typography.Text strong>
        protable{' '}
        <a href="https://protable.ant.design/" rel="noopener noreferrer" target="__blank">
          example
        </a>
      </Typography.Text>
      <CodePreview>yarn add @ant-design/pro-table</CodePreview>
      <Typography.Text
        strong
        style={{
          marginBottom: 12,
        }}
      >
        prolayout{' '}
        <a href="https://prolayout.ant.design/" rel="noopener noreferrer" target="__blank">
          example
        </a>
      </Typography.Text>
      <CodePreview>yarn add @ant-design/pro-layout</CodePreview>
    </Card>
  </PageContainer>
);
