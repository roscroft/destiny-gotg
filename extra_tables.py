    # Activities
    activity_info = {'values': {
                        'id': [['activityHash']],
                        'activity_name': [['activityName']],
                        'activity_type_hash': [['activityTypeHash']]},
                     'primary_keys': ['id']}
    activity_statement = "SELECT * FROM DestinyActivityDefinition"
    def activity_condition(info):
        """Checks if the object is an activity"""
        return not ("activityName" in info)
    build_reference_table(
        "activity", ActivityReference, activity_statement, activity_info, activity_condition)

    # Activity types
    activity_type_info = {'info':{'id':'activityTypeHash', 'activity_type_name':'activityTypeName'}, 'primary_keys':{'id'}}
    activity_type_statement = "SELECT * FROM DestinyActivityTypeDefinition"
    def activity_type_condition(info):
        """Checks if the object is an activity type"""
        return not "activityTypeName" in info
    build_reference_table("activity type", ActivityTypeReference, activity_type_statement,
                          activity_type_info, activity_type_condition)

    # Buckets
    bucket_table = BucketReference
    bucket_info = {'info':{'id':'bucketHash', 'bucket_name':'bucketName'}, 'primary_keys':{'id'}}
    bucket_statement = "SELECT * FROM DestinyInventoryBucketDefinition"
    def bucket_condition(info):
        """Checks if the object is a bucket"""
        return not "bucketName" in info
    build_reference_table(
        "bucket", bucket_table, bucket_statement, bucket_info, bucket_condition)

