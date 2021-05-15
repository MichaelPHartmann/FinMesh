"""
The goal is to create a way to automate the setting and changing of environment variables through FinMesh.
The current moethdo involves getting into your bash profile and adding your tokens manually. While this is not super complicated, it can be daunting for new users who may not have any experience with bash or Python.
Alternative methods were looked at but they proved to either be more complicated, less secure, or less reliable.
Having tokens referenced in the functions creates a potential security issue if someone pushes tokens onto their GitHub accidentally.
Hidden files (such as dot-prefixed files) are another option, but the user must know how to add gitignore files and if they do not, you again end up with API tokens being pushed public.
Having tokens stored as environment variables makes sense for a few reasons.

First, there is very little chance of someone accidentally pushing secrets because the variables are not stored in repositories themselves.
Second, global environment variables are accessible ANYWHERE, meaning you can have multiple projects in separate directories and you only have to set up your tokens once.
Third, it is a generally accepted good practice for handling sensitive API token data.
"""

# environment setup class
# types of environment variables that can be set as class attributes
# method for ingesting desired variables to be modified or added
# python bash method - subprocess.Popen(bash commands as strings) first import
#
class FinMeshSetup():
    def __init__(self):
        self.variables_to_define = ['IEX_TOKEN', 'IEX_SANDBOX_TOKEN', 'IEX_SANDBOX', 'FRED_TOKEN']

    def _bash_builder(variable, value):
        """Builds a bash command to export the specified variable"""
        command = f'export {variable}={value}'
        return command

    def set_all_environment_variables():
        """Prompts the user to enter all of the needed variables for FinMesh.
        Useful for first-time users who have not set any variables yet.
        If you would like to skip through a particular variable, just hit enter to assign a blank; no variable will be created in your environment."""
