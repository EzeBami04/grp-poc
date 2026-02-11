This workflow is designed to check a repository build a docker image from the existing docker files and also run a vuneralbility scan using grype.

Repository structure
The main workflow can be foun in the app.yml within the .github/workflows

Detailed workflow
- checks out code: It checks repository code using the checkout version 4 

- builds an image: Builds a docker image from any existing dockerfile within the root folder 
- performs a container image
- Performs vulnerability scan with Anchore's Grype tool and integrates the results with GitHub Advanced 

Security
- codode scanning feature.  For more information on the Anchore scan action usage and parameters, 

see https://github.com/anchore/scan-action.

information on Anchore's container image scanning tool Grype, see  https://github.com/anchore/grype. It uses actions that are not certified by GitHub. They are provided by a third-party and are governed by separate terms of service, privacy policy, and support documentation.