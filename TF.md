## Use of terraform
- `terraform init`<br/>
- `terraform plan`<br/>
- `terraform apply`<br/>
## Best practices for Terraform
- Don't commit `.tfstate` files
- Back up state files
- Use variable files
`terraform apply -var-file="testing.tfvars"`
