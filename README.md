## Hit Level Data Implementation

### AWS CLI Setup in local Windows

Below is the steps to setup AWSCLI in local machine. 

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
