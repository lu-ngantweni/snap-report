import boto3

def list_snapshots(region):
    """
    Lists all the snapshots in the specified AWS region and categorizes them as either incremental or full.
    
    Args:
        region (str): The AWS region to list the snapshots for.
    """
    # Create an EC2 client for the specified region
    ec2 = boto3.client('ec2', region_name=region)
    
    # Retrieve all the snapshots in the region
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    
    # Categorize the snapshots as either incremental or full
    incremental_snapshots = []
    full_snapshots = []
    for snapshot in snapshots:
        if snapshot['Encrypted']:
            incremental_snapshots.append(snapshot)
        else:
            full_snapshots.append(snapshot)
    
    # Print the results
    print(f"Snapshots in {region}:")
    print("Incremental snapshots:")
    for snapshot in incremental_snapshots:
        print(f"  - {snapshot['SnapshotId']}")
    print("Full snapshots:")
    for snapshot in full_snapshots:
        print(f"  - {snapshot['SnapshotId']}")

# Example usage
list_snapshots('us-east-1')
