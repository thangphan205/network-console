import { Settings as ProSettings } from '@ant-design/pro-layout';

type DefaultSettings = ProSettings & {
  pwa: boolean;
  siderWidth: number;
};

const proSettings: DefaultSettings = {
  navTheme: 'dark',
  primaryColor: '#1890ff',
  layout: 'side',
  contentWidth: 'Fluid',
  fixedHeader: false,
  fixSiderbar: true,
  siderWidth: 256,
  colorWeak: false,
  menu: {
    locale: true,
  },
  title: 'Network Console',
  pwa: false,
  iconfontUrl: '',
};

export type { DefaultSettings };

export default proSettings;
