#Git 
A pull request is a proposal to merge changes from one branch into another. It's a widely-used method for creating and reviewing code. In this section, I'll guide you through the process of creating a pull request using the GitHub website.

For instance, let's say you have a branch named `feature-branch` and you want to merge it into the `main` branch. We'll walk you through how to create a pull request for this scenario. Let's get started.

First, let's make a change to our feature branch by adding a file to it:

```bash

$ git checkout feature-branch

```

You should see something like this in your terminal:

```bash

git checkout feature-branch
Switched to a new branch 'feature-branch'
branch 'feature-branch' set up to track 'origin/feature-branch'.

```

Now, let's add a file to the feature branch.

```bash

$ touch feature-branch-file.txt

```

After running the command, you should see a new file called `feature-branch-file.txt` in your directory.

The `touch` command is used to create a new file. Replace `feature-branch-file.txt` with the name of your file. In this case, we're creating a new file called `feature-branch-file.txt`.

Now, let's add some content to the file.

```bash

$ echo "This is a file in the feature branch" >> feature-branch-file.txt

```

This command adds the text "This is a file in the feature branch" to the `feature-branch-file.txt` file.

The `echo` command is used to add content to a file. In this case, we're adding the text "This is a file in the feature branch" to the `feature-branch-file.txt` file.

Now that we have some text in the file, let's stage and commit the changes to the feature branch.

```bash

$ git add .

```

The `git add .` command stages all the changes in the current directory.

```bash


$ git commit -m "Add file to feature branch"

```

The `git commit -m` command commits the changes to the current branch. Replace `Add file to feature branch` with your own descriptive message. This message should provide a brief summary of the changes you've made. In this case, we're committing the changes to the feature branch.

Now, let's push the changes to the remote repository on GitHub.

```bash

$ git push origin feature-branch

```

The `git push` command is used to push changes from your local repository to the remote repository on GitHub. Replace `feature-branch` with the name of your branch. In this case, we're pushing the changes to the `feature-branch` branch.

_Congratulations!_ You have successfully pushed your changes to the remote repository on GitHub. You can now view your changes on the GitHub website.

Now when you open your GitHub repository, you should see a message indicating that you recently pushed a new branch. You can click on the `Compare & pull request` button to create a pull request for the `feature-branch` branch.