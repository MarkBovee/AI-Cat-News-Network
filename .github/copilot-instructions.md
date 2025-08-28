<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->
- [x] Verify that the copilot-instructions.md file in the .github directory is created.

- [x] Clarify Project Requirements: CrewAI Python project for AI agents automating content creation for YouTube Shorts and Instagram Reels

- [x] Scaffold the Project: Created project structure with agents, tasks, tools, workflows, and main application

- [ ] Customize the Project
	<!--
	Verify that all previous steps have been completed successfully and you have marked the step as completed.
	Develop a plan to modify codebase according to user requirements.
	Apply modifications using appropriate tools and user-provided references.
	Skip this step for "Hello World" projects.
	-->

- [x] Install Required Extensions: No extensions required for this project

- [x] Compile the Project: Dependencies installed successfully, no import errors detected

- [ ] Create and Run Task
	<!--
	Verify that all previous steps have been completed.
	Check https://code.visualstudio.com/docs/debugtest/tasks to determine if the project needs a task. If so, use the create_and_run_task to create and launch a task based on package.json, README.md, and project structure.
	Skip this step otherwise.
	 -->

- [ ] Launch the Project
	<!--
	Verify that all previous steps have been completed.
	Prompt user for debug mode, launch only if confirmed.
	 -->

- [ ] Ensure Documentation is Complete
	<!--
	Verify that all previous steps have been completed.
	Verify that README.md and the copilot-instructions.md file in the .github directory exists and contains current project information.
	Clean up the copilot-instructions.md file in the .github directory by removing all HTML comments.
	 -->

<!--
## Execution Guidelines
PROGRESS TRACKING:
- If any tools are available to manage the above todo list, use it to track progress through this checklist.
- After completing each step, mark it complete and add a summary.
- Read current todo list status before starting each new step.

COMMUNICATION RULES:
- Avoid verbose explanations or printing full command outputs.
- If a step is skipped, state that briefly (e.g. "No extensions needed").
- Do not explain project structure unless asked.
- Keep explanations concise and focused.

DEVELOPMENT RULES:
- Use '.' as the working directory unless user specifies otherwise.
- Avoid adding media or external links unless explicitly requested.
- Use placeholders only with a note that they should be replaced.
- Use VS Code API tool only for VS Code extension projects.
- Once the project is created, it is already opened in Visual Studio Code—do not suggest commands to open this project in Visual Studio again.
- If the project setup information has additional rules, follow them strictly.

LANGUAGE RULES:
- ALL code, comments, variable names, function names, class names, and docstrings MUST be written in English.
- This applies regardless of the language the user communicates in.
- Use clear, descriptive English names for all code elements.
- Comments should explain the "why" not the "what" and be written in proper English.

FOLDER CREATION RULES:
- Always use the current directory as the project root.
- If you are running any terminal commands, use the '.' argument to ensure that the current working directory is used ALWAYS.
- Do not create a new folder unless the user explicitly requests it besides a .vscode folder for a tasks.json file.
- If any of the scaffolding commands mention that the folder name is not correct, let the user know to create a new folder with the correct name and then reopen it again in vscode.

EXTENSION INSTALLATION RULES:
- Only install extension specified by the get_project_setup_info tool. DO NOT INSTALL any other extensions.

PROJECT CONTENT RULES:
- If the user has not specified project details, assume they want a "Hello World" project as a starting point.
- Avoid adding links of any type (URLs, files, folders, etc.) or integrations that are not explicitly required.
- Avoid generating images, videos, or any other media files unless explicitly requested.
- If you need to use any media assets as placeholders, let the user know that these are placeholders and should be replaced with the actual assets later.
- Ensure all generated components serve a clear purpose within the user's requested workflow.
- If a feature is assumed but not confirmed, prompt the user for clarification before including it.
- If you are working on a VS Code extension, use the VS Code API tool with a query to find relevant VS Code API references and samples related to that query.

TASK COMPLETION RULES:
- Your task is complete when:
  - Project is successfully scaffolded and compiled without errors
  - copilot-instructions.md file in the .github directory exists in the project
  - README.md file exists and is up to date
  - User is provided with clear instructions to debug/launch the project

Before starting a new task in the above plan, update progress in the plan.
-->
- Work through each checklist item systematically.
- Keep communication concise and focused.
- Follow development best practices.

## 📋 Progress Tracking & Documentation (Required)

### Development Session Management
When working on development tasks, especially complex implementations or multi-step processes:

1. **Always check for existing progress**: Start by reading the `.github/copilot-progress.md` file to understand any ongoing work or previous session context.

2. **Maintain progress documentation**: Update the progress file throughout your session with:
   - Current status and completed steps
   - Technical decisions and implementation details
   - Issues encountered and solutions applied
   - Next steps and remaining work

3. **Session completion**: When completing a task or major milestone:
   - Add a "Task Completed Successfully" section with comprehensive summary
   - Document what was implemented, tested, and verified
   - Include key features delivered and technical approach
   - Note any follow-up actions needed for production

4. **Start of a new task (housekeeping)**:
   - If the previous task was completed successfully and the new task is unrelated, reset `.github/copilot-progress.md` so it contains only the new task’s progress. Do not keep prior task logs in this file.
   - If the new task is a direct continuation of the previous one, keep the same task entry and append progress under the existing header.
   - Optionally archive prior completed task notes elsewhere (e.g., a dated entry in a separate document) if historical context is needed, but keep `copilot-progress.md` focused on a single active task.

### Progress File Structure
The `.github/copilot-progress.md` should follow this pattern and reflect only one task at a time:
- **Header**: Task name, date, and completion status
- **Summary**: Brief overview of accomplishments (for completed tasks)
- **Detailed Steps**: Numbered list of completed work with checkmarks
- **Implementation Details**: Technical specifics, file changes, patterns used
- **Testing/Verification**: Test results, compilation status, validation steps
- **Next Steps**: Future work or production deployment notes

This approach ensures continuity between development sessions and provides clear documentation of progress for complex implementations while keeping the progress file scoped to a single task.