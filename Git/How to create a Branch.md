#Git 
Branching is a fundamental concept in Git. It allows you to diverge from the main line of development and continue working without impacting the main codebase.

In this section, I'll guide you through the process of creating a new branch using the `git branch` command. This command creates a new branch but does not switch to it. In the following steps, we'll also cover how to switch to your newly created branch using the `git checkout` command. Let's dive in.

To create a new branch, you need to follow these steps:

1. Open your terminal and navigate to the directory of your local repository.
    
2. Use the `git branch` command to create a new branch. Replace `<branch-name>` with the name of your new branch.
```
git branch <branch-name>  # ex. git branch feature- 
                          # branch
```
The `git branch` command creates a new branch but does not switch to it. To switch to your newly created branch, use the `git checkout` command.
```
git checkout <branch-name>
```
The `git checkout` command is used to switch from one branch to another. Replace `<branch-name>` with the name of your new branch. In this case, we're switching to the `feature-branch` branch. But we if want to delete the branch, we can use the following command:
```
# Delete a branch
git branch -d <branch-name>
```
The `git branch -d` command is used to delete a branch. Replace `<branch-name>` with the name of the branch you want to delete. In this case, we're deleting the `feature-branch` branch.

_Congratulations!_ You have successfully created a new branch and switched to it. You can now start adding files and making changes to your new branch.