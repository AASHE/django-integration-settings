## Constant Integration Settings

This provides templates and documentation for setting up integrations with travis.ci and coveralls.io.

## Configuration
    
    - On github, enable travis.ci in your repository's settings.
    - On travis.ci, make sure the repository is displayed and is enabled.
    - On coveralls.io, add your repository. Copy the repo token provided for later 
    use in your .coveralls.yml file.
    - Create a .travis.yml file in your project's root directory. See template.
    - Create a .coveragerc file in your project's root directory. See template.
    - Create a .coverally.yml file in your project's root directory. See template.
    - Commit and push to github. Build on travis.ci should occur automatically. 
    Coveralls data will take a few minutes to be populated.
    
    Note: Remember to remove the instructional comment lines from these configuration files.
    
## Troubleshooting

    - If builds are not triggering with travis, check your repository settings on github and travis.ci. 
    Be sure travis is set to build on each push and/or pull request.
    - Coveralls is sometimes touchy about the omit line in the .coveragerc file. See their
    documentation for more details.
