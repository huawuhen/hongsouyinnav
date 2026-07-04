# AIGC导航站

这是一个中文 AIGC 工具导航站，部署域名为 `nav.redith.cn`。

当前站点只保留中文页面，首页默认进入 `cn/index.html`。导航内容参考工具达人 AI 导航，按当前模板容量整理为 241 个 AI/AIGC 相关站点，覆盖 AI 对话、写作办公、智能体、绘画设计、音乐语音、视频数字人、编程开发、学习资料、运营工具等方向。

## 项目特性

- 纯静态站点，不依赖 Node.js 构建。
- 根路径 `index.html` 会自动跳转到 `cn/index.html`。
- 站点资源全部在 `assets/` 和 `cn/` 目录中。
- 可直接部署到 Cloudflare Pages、EdgeOne Pages、GitHub Pages、Nginx 或任意静态托管服务。

## 本地预览

```bash
python3 -m http.server 8123
```

打开：

```text
http://localhost:8123/
```

## 目录

- `index.html`：根入口，默认跳转中文首页。
- `cn/index.html`：中文 AIGC 导航首页。
- `cn/about.html`：关于本站。
- `assets/`：静态样式、脚本、字体和默认图标资源。

## Cloudflare Pages 部署教程

### 方式一：连接 GitHub 仓库部署

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)。
2. 进入 `Workers & Pages`，点击 `Create application`。
3. 选择 `Pages`，再选择 `Connect to Git`。
4. 授权并选择仓库 `huawuhen/hongsouyinnav`。
5. 构建配置填写：
   - Project name：`hongsouyinnav`
   - Production branch：`main`
   - Framework preset：`None`
   - Build command：留空
   - Build output directory：`/`
6. 点击 `Save and Deploy`。
7. 部署完成后，在 `Custom domains` 中绑定自定义域名，例如 `nav.redith.cn`。

### 方式二：直接上传部署

1. 登录 Cloudflare Dashboard。
2. 进入 `Workers & Pages`，点击 `Create application`。
3. 选择 `Pages`，再选择 `Upload assets`。
4. 项目名填写 `hongsouyinnav`。
5. 上传本仓库根目录下的静态文件和目录：
   - `index.html`
   - `404.html`
   - `CNAME`
   - `cn/`
   - `assets/`
   - `scripts/`
6. 发布后在 Pages 项目中绑定自定义域名。

## EdgeOne Pages 部署教程

本项目已适配 EdgeOne Pages / EdgeOne Makers CLI 的静态站点部署方式，不需要构建命令。

### 准备 CLI

```bash
npm install -g edgeone@latest
PAGES_SOURCE=skills edgeone -v
```

建议 CLI 版本不低于 `1.6.0`。

### 登录账号

中国站：

```bash
PAGES_SOURCE=skills edgeone login --site china
```

国际站：

```bash
PAGES_SOURCE=skills edgeone login --site global
```

检查登录状态：

```bash
PAGES_SOURCE=skills edgeone whoami
```

### 部署到全球可用区

全球加速区域：

```bash
PAGES_SOURCE=skills edgeone makers deploy -n hongsouyinnav --area global --json
```

全球可用区，不含中国大陆：

```bash
PAGES_SOURCE=skills edgeone makers deploy -n hongsouyinnav --area overseas --json
```

部署成功后，命令会返回 JSON，其中：

- `url`：线上访问地址。
- `projectId`：EdgeOne Pages 项目 ID。
- `deploymentId`：本次部署 ID。
- `consoleUrl`：控制台部署详情地址。

### 自定义域名

在 EdgeOne Pages 控制台进入项目后，打开自定义域名配置，绑定 `nav.redith.cn` 或其他域名，并按控制台提示添加 DNS 记录。DNS 生效后即可通过自定义域名访问站点。

## 其他说明

这是纯静态站点，不需要构建步骤。部署到 GitHub Pages、Nginx 或任意静态托管服务即可。
