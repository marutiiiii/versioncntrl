print("sanjivani")



















































 Install Git (if not installed)

sudo apt update
sudo apt install git -y
Verify installation:


git --version
2. Configure Git (First-Time Setup)
Set your GitHub username and email:


git config --global user.name "YourGitHubUsername"
git config --global user.email "YourEmail@example.com"
Verify:


git config --list


3. Create a New Repository on GitHub
Go to GitHub and log in.
Click on New Repository.
Name the repository, choose Public/Private, and click Create Repository.
Copy the repository HTTPS or SSH URL.
4. Initialize a Local Repository
Navigate to the folder where you want to store your project:


cd ~/Documents  # Change to your desired directory
mkdir my_project
cd my_project
Initialize Git:


git init
5. Add a File
Create a sample file:

bash
Copy
Edit
echo "Hello, GitHub!" > hello.txt
Add it to Git:


git add hello.txt
Commit changes:


git commit -m "Initial commit"
6. Link Local Repository to GitHub
Replace <your-repo-url> with the URL copied earlier:


git remote add origin <your-repo-url>
Verify remote:


git remote -v
7. Push File to GitHub

git branch -M main  # Rename the branch to 'main' if needed
git push -u origin main
8. Verify on GitHub
Go to your GitHub repository and check if the file is uploaded.

Next Time: How to Push Updates
Whenever you make changes:


git add .
git commit -m "Updated file"
git push origin main
