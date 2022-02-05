## Hit Level Data Implementation

### AWS CLI Setup in local Windows

Below are the steps to setup AWSCLI in local machine. 

1. Sign in to the IAM console as Root User
2. Choose Users, Security Credentials and then create access key. Copy Access Key ID & Secret Access Key
3. Install AWSCLI using msi installer in windows. 
   ```sh
   msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
   ```
4. Open command prompt and locate awscli installation folder.
   ```sh
   cd c:\Program Files\Amazon\AWSCLIV2
   ```
5. Run "aws version"
   ```sh
   c:\Program Files\Amazon\AWSCLIV2> aws --version
   aws-cli/2.4.16 Python/3.8.8 Windows/10 exe/AMD64 prompt/off
   ```
6. Run "aws configure" and provide the access key details.
   ```sh
   c:\Program Files\Amazon\AWSCLIV2> aws configure
   AWS Access Key ID [None]: xxxxxxxxxxxxxxxxx
   AWS Secret Access Key [None]: xxxxxxxxx/xxxxxxxxxxx
   Default region name [None]: us-east-1
   Default output format [None]: json
   ```
7. Run "aws s3 ls" to view the s3 buckets
   ```sh
   c:\Program Files\Amazon\AWSCLIV2>aws s3 ls
   2022-02-05 11:45:34 aws-us-east-1-test-bucket
   ```
   
 
 ### Setup Terraform to automate the AWS Deployment
 
 #### Prerequisites
 
1. Intsall go 
   ```sh
   https://go.dev/doc/install
   ```
   
#### Installation

Below are the steps to setup Terraform in local machine
 
 1. Open git bash and clone hashicorp repository
   ```sh
   git clone https://github.com/hashicorp/terraform.git
   ```
 2. Navigate to terraform directory
   ```sh
   cd terraform
   ```
 3. Compile the binary to install terraform
   ```sh
   go install
   ```
 4. Verify Installation
   ```sh
   $ terraform -help
		Usage: terraform [global options] <subcommand> [args]
		
		The available commands for execution are listed below.The primary workflow commands are given first, followed by less common or more advanced commands.
		
		Main commands:
			init          Prepare your working directory for other commands
			validate      Check whether the configuration is valid
			plan          Show changes required by the current configuration
			apply         Create or update infrastructure
			destroy       Destroy previously-created infrastructure
   ```
