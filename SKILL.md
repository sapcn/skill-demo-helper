---
name: skill-demo-helper
description: Skill 试用和解读助手。当用户刚安装一个新的 skill 时，使用此 skill 来：1) 解读这个 skill 的用途和触发词，2) 找到 SKILL.md 并分析其内容，3) 帮助用户理解这个 skill 的结构，4) 提供一个简单的使用示例，5) 验证 skill 是否正常工作。触发词：解读skill、试用skill、这个skill是做什么的、帮我测试这个skill。
---

# Skill Demo Helper - Skill 试用助手

## 目的

帮助用户理解并验证刚安装的新 skill 是否靠谱。

## 工作流程

当用户说"解读这个 skill"或"试用这个 skill"时：

### 第一步：定位 Skill

确认 skill 的安装路径：
- Windows: `%USERPROFILE%\.claude\skills\<skill-name>\`
- 或询问用户 skill 的名称

### 第二步：读取 SKILL.md

读取并分析 skill 的主文件：
```bash
# 查找 SKILL.md
cat <skill-path>/SKILL.md
```

### 第三步：解读内容

向用户解释：
1. **Skill 名称和描述** - 这个 skill 是做什么的
2. **触发词** - 什么时候会使用这个 skill
3. **核心功能** - 主要提供什么能力
4. **资源文件** - 有哪些 scripts/references/assets

### 第四步：提供示例

基于 skill 的描述，建议一个简单的试用场景，例如：
- 如果是 PDF skill：建议"帮我提取这个 PDF 的文本"
- 如果是前端 skill：建议"帮我创建一个登录页面"
- 如果是通用 skill：给一个典型的使用示例

### 第五步：验证检查

检查 skill 是否符合基本标准：
- [ ] 有有效的 YAML frontmatter（name 和 description）
- [ ] description 清楚说明了触发场景
- [ ] 没有冗余的 README/INSTALL 等文件
- [ ] 资源文件组织合理

## 使用示例

```
用户：帮我解读一下 deep-research 这个 skill

Claude：
1. 找到 SKILL.md 并读取
2. 解读：这是一个深度调研 skill，用于将模糊主题转化为调研报告
3. 触发词：深度调研、调研一下、写调研报告
4. 建议试用："帮我调研一下 AI 在医疗领域的应用"
5. 验证结果：符合 skill-creator 标准
```

## 注意事项

- 解读时要简洁，避免重复 SKILL.md 的内容
- 示例要简单、具体、易于执行
- 如果 skill 有问题，指出具体问题
