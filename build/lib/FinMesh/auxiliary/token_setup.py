"""
The goal is to create a way to automate the setting and changing of environment variables through FinMesh.
The current method involves getting into your bash profile and adding your tokens manually. While this is not super complicated, it can be daunting for new users who may not have any experience with bash or Python.
Alternative methods were looked at but they proved to either be more complicated, less secure, or less reliable.
Having tokens referenced in the functions creates a potential security issue if someone pushes tokens onto their GitHub accidentally.
Hidden files (such as dot-prefixed files) are another option, but the user must know how to add gitignore files and if they do not, you again end up with API tokens being pushed public.
Having tokens stored as environment variables makes sense for a few reasons.

First, there is very little chance of someone accidentally pushing secrets because the variables are not stored in repositories themselves.
Second, global environment variables are accessible ANYWHERE, meaning you can have multiple projects in separate directories and you only have to set up your tokens once.
Third, it is a generally accepted good practice for handling sensitive API token data.
"""

import subprocess
import time


# python bash method - subprocess.Popen(bash commands as strings) first import

class FinMeshSetup():
    def __init__(self):
        self.tokens_to_define = ['IEX_TOKEN', 'IEX_SANDBOX_TOKEN', 'FRED_TOKEN']
        self.booleans_to_define = ['IEX_SANDBOX_BOOL']

    def _arg_to_bool(self, string):
        affirmative = ['True','TRUE','true','Yes','YES','yes','On','ON','on']
        if string in affirmative:
            return True
        else:
            return False

    def _bash_builder(self, variable, value):
        """Builds a bash command to export the specified variable"""
        command = f'export {variable}={value}'
        return command

    def set_all_environment_variables(self):
        """Prompts the user to enter all of the needed variables for FinMesh.
        Useful for first-time users who have not set any variables yet.
        If you would like to skip through a particular variable, just hit enter to assign a blank; no variable will be created in your environment."""
        cmd_to_run = []
        print("Setting tokens, prepare to paste in tokens when prompted...")
        time.sleep(2)
        for variable in self.tokens_to_define:
            token = input(f"Setting the {variable} variable. Please enter the desired value. Hit enter to skip."
            if token == "":
                pass
            else:
                cmd = self._bash_builder(variable, token)
                cmd_to_run.append(cmd)
        print("Setting booleans, prepare to paste in tokens when prompted...")
        time.sleep(2)
        for variable in self.booleans_to_define:
            bool_input = input(f"Would you like to set {variable} to True? Hit enter to skip.")
            if bool_input == "":
                pass
            else:
                if self._arg_to_bool(bool_input):
                    bool_set = 'TRUE'
                else:
                    boll_set = 'FALSE'
                cmd = _bash_builder(variable, token)
                cmd_to_run.append(cmd)

        for c in cmd_to_run:
            subprocess.Popen(c)
        return cmd_to_run

    def set_IEX_sandbox(onoff):
        if self._arg_to_bool():
            cmd = _bash_builder("IEX_SANDBOX_BOOL", "TRUE")
        else:
            cmd = _bash_builder("IEX_SANDBOX_BOOL", "FALSE")
        subprocess.Popen(cmd)
