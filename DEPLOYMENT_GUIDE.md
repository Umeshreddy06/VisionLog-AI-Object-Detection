# Deployment & Submission Guide

## A. GitHub

Create a **public** repository named:

`Real-Time-Object-Detection`

Upload all project files except `.env`.

Repository URL format:

`https://github.com/YOUR-USERNAME/Real-Time-Object-Detection`

## B. Streamlit deployment

Use Streamlit Community Cloud and select:

- Repository: your GitHub repository
- Branch: `main`
- Main file: `main.py`

After deployment, the platform gives a URL similar to:

`https://your-project-name.streamlit.app`

Copy that URL for the assignment.

## C. Database

A cloud deployment cannot connect to MySQL running on your personal PC at `localhost`.

For a genuinely deployed database, use a remotely reachable MySQL provider and put those credentials in Streamlit secrets. Do not expose the password in GitHub.

## D. Final submission

Submit:

1. GitHub URL
2. Streamlit deployment URL
3. Demo video URL
4. Medium article URL

Do not use placeholder URLs in the final Google Form.
