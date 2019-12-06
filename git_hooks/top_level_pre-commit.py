#!/usr/bin/python
import os, sys

cur_path = os.path.dirname(__file__)
git_hooks_path = os.path.join(cur_path,"..","..","git_hooks","pre_commit")
for hook_file in os.listdir(git_hooks_path):
	result = os.system("cd {}; ./{}".format(git_hooks_path, hook_file))
	if result != 0:
		sys.exit(result)
