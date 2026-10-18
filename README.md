# Dramagic Skills

用你熟悉的 AI Agent，为 Dramagic 制作自己的角色包。

描述角色的外观、性格、职业和故事用途，让 Agent 根据规格制作头像、全身图、四种表情立绘及角色数据，打包成 `.dramagic-character-pack` 文件，再导入 Dramagic 创作者工作台。无需手工编写角色清单，也不需要预生成多语言音频。

## 1. 安装 Skills

在希望制作角色包的项目目录打开终端，运行：

```sh
npx skills add https://github.com/tentacle-pro/dramagic-skills
```

按安装器提示选择支持的 Agent 和项目级安装位置。需要 Node.js/npm，以及访问 GitHub 的网络连接。安装不会自动赋予 Agent 生图、搜索或文件执行能力。

### 不熟悉命令？复制给 Agent

把下面这段话发给你使用的 Agent App：

```text
请帮我在当前项目中安装 Dramagic 角色制作 Skills：
https://github.com/tentacle-pro/dramagic-skills

如果你能执行终端命令，请在我确认的项目目录运行：
npx skills add https://github.com/tentacle-pro/dramagic-skills
按当前软件支持的方式安装本仓库的三个 Skills，不要默认全局安装。

如果你不能执行命令或不支持 Skills 自动安装，请说明限制，
指导我下载仓库，并按你的软件支持的方式添加 SKILL.md 及其 references。
制作和打包时也需要访问仓库 tools/；不要声称安装了你无法访问的文件。
```

可以在 ChatGPT App、Claude Desktop、豆包、WorkBuddy 或其他 Agent 环境中尝试。**是否能直接安装、生成图片及导出文件，取决于该软件的版本、Skills 支持和已启用工具；本项目并未逐一验证这些 App。** 纯聊天模式可辅助设计，但未必能独立生成可导入文件；没有终端、图像或文件能力时，需要人工操作或相应工具配合。

## 2. 告诉 Agent 你想要什么角色

安装后可以直接说：

```text
请使用 Dramagic Skills，帮我制作一个原创角色包：
角色是海边潮汐观测站的夜班管理员 Mara Venn，银色发辫、
锈橙色防水外套，随身带黄铜潮位仪；性格沉静，带一点冷幽默。
用于与旅客沟通暴风雨期间的出行安排，风格为精致游戏角色立绘。

请生成头像、完整全身招牌图，以及常态、微笑、愤怒、动摇四种
透明背景半身表情图，选择匹配的 Gemini 音色，并完成角色数据。
请先询问我的作者 ID、包 ID 和发行版本，不要使用官方身份。
最终交付 .dramagic-character-pack 文件；提示词、过程文件和报告放包外。
请分别报告实际图片质检和角色包校验结果，缺少工具时明确说明。
```

也可以描述一组角色、自己的世界观，或提供你有权使用的现成素材。Skills 不绑定特定图像模型：Agent 可按实际能力搜索合适来源、生成或加工图片，但应保证素材使用权限与角色视觉一致性。生成服务可能需要登录、额度或付费，执行前由你与 Agent 确认。

每个角色包含头像、完整全身图及四种半身表情，使用 WebP；表情立绘需真实透明背景。口头禅只保存文本：导入 App 后，Dramagic 根据所选学习目标语言与角色音色，通过 Gemini Live 翻译并发声（需要联网及相应服务可用）。

## 3. 导入 Dramagic

1. 获取 Agent 交付的 `.dramagic-character-pack` 文件。
2. 打开 **Dramagic → 创作者工作台 → 打开剧本画布 → 演职员表 → 官方选角中心 → 导入角色包**。
3. 选择文件，检查作者、包名、版本和角色数量，然后确认导入。
4. 在“用户导入”分组中浏览、试听并招募角色到自己的剧本。

导入时 App 会再次校验格式、素材和安全限制；失败时把具体报错交给 Agent 修复，不要只修改扩展名或绕过校验。导入只安装到本机，不会自动发布到剧本大厅。已招募并保存到项目的角色素材独立于源角色包。

## 仓库里有什么

| Skill | 职责 |
|---|---|
| [dramagic-character-pack](skills/dramagic-character-pack/SKILL.md) | 角色设定、人格、音色匹配与 3.0 清单 |
| [dramagic-character-art](skills/dramagic-character-art/SKILL.md) | 六张图的规格、视觉一致性与透明边缘质检 |
| [dramagic-character-release](skills/dramagic-character-release/SKILL.md) | 引用白名单打包、校验与交付 |

[格式规范](skills/dramagic-character-pack/references/format.md)、机器可读 schema 和音色描述随仓库提供。`tools/` 是共享打包辅助工具；只安装单个 Skill 的软件可能不会复制它，制作时请让 Agent 下载/访问完整仓库。规则以成品规格为主，不要求固定生图供应商或复杂处理流水线。

## 打包与校验工具

可选打包器需要 Node.js 与 Python 3.10+ 标准库。在本仓库根目录运行：

```sh
node tools/package.mjs RELEASE_DIRECTORY OUTPUT.dramagic-character-pack
```

打包器只收集清单引用的图片，不包含提示词、旧音频或过程文件，并拒绝覆盖已有输出。**装配完成不等于校验通过。** 本仓库目前不附带独立原生校验器二进制；有 Dramagic 客户端源码的维护者可从客户端根目录运行：

```sh
cargo run --manifest-path src-tauri/Cargo.toml --example validate_character_pack -- PACKAGE
```

没有原生校验器时，Agent 应标注“已装配、未做原生校验”，随后由 App 导入校验，不虚称已验证。自动校验也不能代替图片质量、角色一致性和授权的人工检查。

## 许可与使用边界

本仓库按 [CC0 1.0](LICENSE) 提供；它不替生成工具、模型服务或第三方素材授予使用许可。请制作原创或已获得相应授权的角色，遵守所用服务与素材的条款。角色包中的作者声明、成功导入及本地试玩都不是权利认证或官方发布许可。

## 维护与反馈

遇到问题时，提供所用 Agent/工具版本、操作步骤和具体校验错误；不要公开密钥、私人图片或未经授权的素材。首次使用建议制作一个与官方角色明显不同的新角色，便于确认来源并验证招募、保存及剧本交换。
