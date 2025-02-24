Source from: https://help.tower.nf/22.2/compute-envs/google-cloud/

This guide assumes you have an existing Google Cloud account. Sign up for a free account [here](https://cloud.google.com/).

## Create a project
Navigate to the [Google Project Selector page](https://console.cloud.google.com/projectselector2) and either select an existing project or select **Create project**.

Enter a name for your new project, e.g "my-gcp-project-1234".

If you are part of an organization, the location will default to your organization.

## Enable billing
In the navigation menu `(≡)`, select Billing. You can follow [these instructions](https://cloud.google.com/billing/docs/how-to/modify-project) to enable billing.

## Enable APIs <a name = "EA"></a>
Use this [link](https://console.cloud.google.com/flows/enableapi?apiid=lifesciences.googleapis.com%2Ccompute.googleapis.com%2Cstorage-api.googleapis.com) to enable the following APIs for your project:

- Cloud Life Sciences API
- Compute Engine API
- Cloud Storage API

Select your project from the dropdown menu and select __Enable__.

Alternatively, you can enable each API manually by selecting your project in the navigation bar and visiting each API page:

- [Cloud Life Sciences API](https://console.cloud.google.com/marketplace/product/google/lifesciences.googleapis.com)
- [Compute Engine API](https://console.cloud.google.com/marketplace/product/google/compute.googleapis.com)
- [Cloud Storage API](https://console.cloud.google.com/marketplace/product/google/storage-api.googleapis.com)

## Create a Cloud Storage bucket

1. In the navigation menu `(≡)`, select `Cloud Storage` and then __Create bucket__.
2. Enter a name for your bucket. You will reference this name when you need to transfer the output results from the GCP or running the nf-core/methylseq pipeline. You can also upload your own dataset to the bucket to use in GCP. (**NOTE**: Do not use underscores (_) in your bucket name. Use hyphens (-) instead.) 
3. Select __Region__ for the __Location type__ and select the __Location__ for your bucket.
4. Select __Standard__ for the default storage class.
5. Select __Uniform__ for the Access control.
6. Select __Create__.
7. Once the bucket is created, you will be redirected to the Bucket details page.
8. Select Permissions, then + Add.
9. Copy the email address of the Compute Engine default service account into New principals.
10. Select the following roles:
    - Storage Admin
    - Storage Legacy Bucket Owner
    - Storage Legacy Object Owner
    - Storage Object Creator
11. If you have a service account that need to access the bucket, repeat step 9 to enter the service account email, and step 10 to select the following roles:
    - Storage Admin
    - Storage Object Admin

Additional information can be found [here](https://cloud.nih.gov/resources/cloudlab/google-cloud-jumpstart/#sto).

## Create a Nextflow service account <a name="CNSA"></a>
(Only used in Tutorial 4)

1. Enable the Cloud Life Sciences, Compute Engine, and Cloud Storage APIs. (Already done in the [previous step 0.3](#EA))
2. In the navigation menu `(≡)`, select `IAM & Admin` and then `Service Accounts`.
3. Select `CREATE SERVICE ACCOUNT`
4. Type in 'nextflow-service-account' as the service account name and press `Done`
5. On the `AMI & Admin menu` click `IAM` then click edit (pencil icon) next to the Nextflow service account
6. Add the following roles and click `Save`:
    - lifesciences.workflowsRunner
    - iam.serviceAccountUser
    - serviceusage.serviceUsageConsumer
    - storage.objectAdmin

**Create a notebook with Service account Permission**
When creating a notebook you can edit the permissions to utilize the Nextflow service account.

7. In the navigation `IAM & Admin` menu and then select `Service Accounts` (if you aren't there already), locate your Nextflow service account and copy the entire email name
8. Start to create your notebook and edit the Permissions section by **unclicking** `Use Compute Engine default service account` and enter your service account email
9. Click `Create`

**WARNING**: Please do NOT create a service key if instructed by any tutorial. API keys are generally not considered secure; they are typically accessible to clients, making it easy for someone to steal an API key. Once the key is stolen, it has no expiration, so it may be used indefinitely, unless the project owner revokes or regenerates the key.
