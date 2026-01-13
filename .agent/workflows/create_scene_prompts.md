---
description: Create scene prompts from a given topic (Draft -> Review -> Prompts)
---

This workflow standardizes the process of converting a user-provided topic into Stable Diffusion prompts.

# Steps

1. **Understand the Topic**: Read the user's request to understand the core situation and desired "moe" points or fetishes.

2. **Draft Scenes (`scenes_draft.md`)**:
   - Create or update `scenes_draft.md`.
   - List 10 scenes (or requested number).
   - For each scene, define the **Concept** and the following **Visual Elements**:
     - **Background (背景)**
     - **Boy (男の子)** - Expression, action
     - **Woman (女性)** - Expression, action
     - **Clothing (服装)** - Describe for **Woman ONLY**. Must be highly specific (e.g., fabric type, fit, specific garments like 'ribbed knit', 'sheer blouse', 'pencil skirt').
     - **Pose (ポーズ)** - Physical interaction
     - **Angle (アングル)** - Camera position

3. **User Review**:
   - Present the draft to the user using `notify_user`.
   - Ask for confirmation or specific refinements (e.g., "Add more erotic tension", "Change the outfit").

4. **Generate Prompts (`prompts.md`)**:
   - Once the draft is approved, create or update `prompts.md`.
   - Convert the visual elements into specific Stable Diffusion tags (e.g., `1boy, 1girl, shota, older female`).
   - **CRITICAL**: Always include the subject for actions (e.g., `girl waving`, `boy smiling`, `girl hugging boy`) to avoid ambiguity.
   - Use strict quality tags (`masterpiece, best quality`) and negative prompts.
   - Ensure specific elements like 'erection reveal' are translated into effective tags (`bulge`, `tenting`, `pointing`, etc.).

5. **Final Output**:
   - (Optional) Convert the prompts into a YAML format (`pose_scenes.yaml`) if requested.
