import requests

#api_key = "<your api key here>"
#origin_header = "<your origin header here>"
#api_headers_public = {"X-API-Key": api_key, "Origin": origin_header}
#api_headers_private = {"X-API-Key": api_key, "Origin": origin_header, "Authorization: Bearer": access_token}


class ApplicationService(object):
    def __init__(self):
        pass

    def application_search(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ApplicationService/ApplicationSearch
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/App/Search/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def change_api_key_status(self, access_token, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ApplicationService/ChangeApiKeyStatus
        Access: Private  Method: POST
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/App/ChangeApiKeyState/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def create_api_key(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ApplicationService/CreateApiKey
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/App/CreateApiKey/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def create_application(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ApplicationService/CreateApplication
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/App/CreateApplication/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def edit_application(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ApplicationService/EditApplication
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/App/EditApplication/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_access_tokens_from_code(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ApplicationService/GetAccessTokensFromCode
        Access: Public  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/App/GetAccessTokensFromCode/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_access_tokens_from_refresh_token(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ApplicationService/GetAccessTokensFromRefreshToken
        Access: Public  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/App/GetAccessTokensFromRefreshToken/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_application(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ApplicationService/GetApplication
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/App/Application/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_application_api_keys(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ApplicationService/GetApplicationApiKeys
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/App/ApplicationApiKeys/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_authorization_for_user_and_application(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ApplicationService/GetAuthorizationForUserAndApplication
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/App/Authorization/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_authorizations(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ApplicationService/GetAuthorizations
        Access: Private  Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/App/Authorizations/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_o_auth_tokens(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ApplicationService/GetOAuthTokens
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/App/oauth/token/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def private_application_search(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ApplicationService/PrivateApplicationSearch
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/App/PrivateSearch/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def revoke_authorization(self, access_token, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ApplicationService/RevokeAuthorization
        Access: Private  Method: POST
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/App/RevokeAuthorization/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json


class AdminService(object):
    def __init__(self):
        pass

    def admin_user_search(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/AdminUserSearch
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Member/Search/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def bulk_edit_post(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/BulkEditPost
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/BulkEditPost/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_admin_history(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/GetAdminHistory
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/GlobalHistory/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_assigned_reports(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/GetAssignedReports
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Assigned/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_disciplined_reports_for_member(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/GetDisciplinedReportsForMember
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Member/" + param1 + "/Reports/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_recent_discipline_and_flag_history_for_member(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/GetRecentDisciplineAndFlagHistoryForMember
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Member/" + param1 + "/RecentIncludingFlags/" + param2 + ""
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_resolved_reports(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/GetResolvedReports
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Reports/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_user_ban_state(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/GetUserBanState
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Member/" + param1 + "/GetBanState/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_user_post_history(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/GetUserPostHistory
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Member/" + param1 + "/PostHistory/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_user_web_client_ip_history(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/GetUserWebClientIpHistory
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Member/" + param1 + "/GetWebClientIpHistory/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def globally_ignore_item(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/GloballyIgnoreItem
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Ignores/GloballyIgnore/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def override_ban_on_user(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/OverrideBanOnUser
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Member/" + param1 + "/SetBan/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def override_global_ignore(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/OverrideGlobalIgnore
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Ignores/OverrideGlobalIgnore/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def override_group_wall_ban_on_user(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/OverrideGroupWallBanOnUser
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Member/" + param1 + "/SetGroupWallBan/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def override_msg_ban_on_user(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/OverrideMsgBanOnUser
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Member/" + param1 + "/SetMsgBan/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def overturn_report(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/OverturnReport
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Reports/Overturn/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def resolve_report(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/ResolveReport
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Assigned/Resolve/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def return_assigned_reports(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/AdminService/ReturnAssignedReports
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Admin/Assigned/ReturnAll"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json


class ExternalSocialService(object):
    def __init__(self):
        pass

    def get_aggregated_social_feed(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ExternalSocialService/GetAggregatedSocialFeed
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/ExternalSocial/GetAggregatedSocialFeed/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json


class GroupService(object):
    def __init__(self):
        pass

    def approve_all_pending(self, access_token, groupId, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/ApproveAllPending
        Access: Private  Method: POST
        :param groupId: 
        KWARGS values should be "param=value"
        :param message: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/ApproveAll/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def approve_group_membership(self, access_token, groupId, membershipId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/ApproveGroupMembership
        Access: Private  Method: POST
        :param groupId: 
        :param membershipId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/" + membershipId + "/Approve/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def approve_group_membership_v2(self, access_token, groupId, membershipId, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/ApproveGroupMembershipV2
        Access: Private  Method: POST
        :param groupId: 
        :param membershipId: 
        KWARGS values should be "param=value"
        :param message: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/" + membershipId + "/ApproveV2/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def approve_pending_for_list(self, access_token, groupId, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/ApprovePendingForList
        Access: Private  Method: POST
        :param groupId: 
        KWARGS values should be "param=value"
        :param membershipIds: 
        :param message: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/ApproveList/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def ban_member(self, access_token, groupId, membershipId, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/BanMember
        Access: Private  Method: POST
        :param groupId: 
        :param membershipId: 
        KWARGS values should be "param=value"
        :param length: 
        :param comment: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/" + membershipId + "/Ban/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def break_alliance(self, access_token, groupId, allyGroupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/BreakAlliance
        Access: Private  Method: POST
        :param groupId: 
        :param allyGroupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Relationship/" + allyGroupId + "/BreakAlliance/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def break_alliances(self, access_token, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/BreakAlliances
        Access: Private  Method: POST
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/BreakAlliances/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def create_group(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/CreateGroup
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/Create/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def create_group_v2(self, access_token, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/CreateGroupV2
        Access: Private  Method: POST
        KWARGS values should be "param=value"
        :param avatarImageIndex: 
        :param clanCallSign: 
        :param membershipOption: 
        :param attributes: 
        :param isPublic: 
        :param isDefaultPostPublic: 
        :param clanMembershipTypes: 
        :param locale: 
        :param theme: 
        :param clanName: 
        :param motto: 
        :param name: 
        :param clanReviewType: 
        :param allowChat: 
        :param tags: 
        :param about: 
        :param isPublicTopicAdminOnly: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/Create/V2/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def create_minimal_group(self, access_token, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/CreateMinimalGroup
        Access: Private  Method: POST
        KWARGS values should be "param=value"
        :param groupName: 
        :param groupAbout: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/Create/Minimal/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def deny_all_pending(self, access_token, groupId, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/DenyAllPending
        Access: Private  Method: POST
        :param groupId: 
        KWARGS values should be "param=value"
        :param message: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/DenyAll/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def deny_group_membership(self, access_token, groupId, membershipId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/DenyGroupMembership
        Access: Private  Method: POST
        :param groupId: 
        :param membershipId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/" + membershipId + "/Deny/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def deny_group_membership_v2(self, access_token, groupId, membershipId, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/DenyGroupMembershipV2
        Access: Private  Method: POST
        :param groupId: 
        :param membershipId: 
        KWARGS values should be "param=value"
        :param message: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/" + membershipId + "/DenyV2/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def deny_pending_for_list(self, access_token, groupId, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/DenyPendingForList
        Access: Private  Method: POST
        :param groupId: 
        KWARGS values should be "param=value"
        :param membershipIds: 
        :param message: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/DenyList/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def designate_clan_founder(self, access_token, param3, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/DesignateClanFounder
        Access: Private  Method: POST
        :param param3: 
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + param1 + "/DesignateClanFounder/" + param2 + "/" + param3 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def disable_clan_for_group(self, access_token, groupId, clanMembershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/DisableClanForGroup
        Access: Private  Method: POST
        :param groupId: 
        :param clanMembershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Clans/Disable/" + clanMembershipType + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def disband_alliance(self, access_token, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/DisbandAlliance
        Access: Private  Method: POST
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/BreakAllAlliances/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def edit_group(self, access_token, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/EditGroup
        Access: Private  Method: POST
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Edit/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def edit_group_membership(self, access_token, groupId, membershipId, groupMembershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/EditGroupMembership
        Access: Private  Method: POST
        :param groupId: 
        :param membershipId: 
        :param groupMembershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/" + membershipId + "/SetMembershipType/" + groupMembershipType + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def edit_group_v2(self, access_token, groupId, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/EditGroupV2
        Access: Private  Method: POST
        :param groupId: 
        KWARGS values should be "param=value"
        :param avatarImageIndex: 
        :param clanCallSign: 
        :param isDefaultPostPublic: 
        :param isPublic: 
        :param membershipOptions: 
        :param homepage: 
        :param motto: 
        :param isPublicTopicAdminOnly: 
        :param clanMembershipTypes: 
        :param enableInvitationMessagingForAdmins: 
        :param theme: 
        :param clanName: 
        :param clanReviewType: 
        :param allowChat: 
        :param defaultPublicity: 
        :param chatSecurity: 
        :param name: 
        :param tags: 
        :param locale: 
        :param about: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/EditV2/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def enable_clan_for_group(self, access_token, groupId, clanMembershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/EnableClanForGroup
        Access: Private  Method: POST
        :param groupId: 
        :param clanMembershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Clans/Enable/" + clanMembershipType + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def follow_groups_with_group(self, access_token, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/FollowGroupsWithGroup
        Access: Private  Method: POST
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/FollowList/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def follow_group_with_group(self, access_token, groupId, followGroupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/FollowGroupWithGroup
        Access: Private  Method: POST
        :param groupId: 
        :param followGroupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Follow/" + followGroupId + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_admins_of_group(self, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetAdminsOfGroup
        Access:   Method: GET
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Admins/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_admins_of_group_v2(self, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetAdminsOfGroupV2
        Access: Public  Method: GET
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/AdminsV2/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_all_founded_groups_for_member(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetAllFoundedGroupsForMember
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/User/" + param1 + "/Founded/All/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_all_groups_for_current_member(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetAllGroupsForCurrentMember
        Access: Private  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/MyGroups/All/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_all_groups_for_member(self, membershipId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetAllGroupsForMember
        Access: Public  Method: GET
        :param membershipId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/User/" + membershipId + "/All/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_allied_groups(self, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetAlliedGroups
        Access: Public  Method: GET
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Allies/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_available_avatars(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetAvailableAvatars-(Group)
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/GetAvailableAvatars/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_available_themes(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetAvailableThemes-(Group)
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/GetAvailableThemes/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_banned_members_of_group(self, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetBannedMembersOfGroup
        Access:   Method: GET
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Banned/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_banned_members_of_group_v2(self, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetBannedMembersOfGroupV2
        Access: Private  Method: GET
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/BannedV2/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_clan_attribute_definitions(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetClanAttributeDefinitions
        Access: Public  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/GetClanAttributeDefinitions/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_deleted_groups_for_current_member(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetDeletedGroupsForCurrentMember
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/MyGroups/Deleted/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_founded_groups_for_member(self, currentPage, membershipId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetFoundedGroupsForMember
        Access:   Method: GET
        :param currentPage: 
        :param membershipId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/User/" + membershipId + "/Founded/" + currentPage + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_group(self, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetGroup
        Access:   Method: GET
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_group_by_name(self, groupName):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetGroupByName
        Access:   Method: GET
        :param groupName: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/Name/" + groupName + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_groups_followed_by_group(self, groupId, currentPage):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetGroupsFollowedByGroup
        Access:   Method: GET
        :param groupId: 
        :param currentPage: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Following/" + currentPage + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_groups_following_group(self, groupId, currentPage):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetGroupsFollowingGroup
        Access:   Method: GET
        :param groupId: 
        :param currentPage: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/FollowedBy/" + currentPage + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_group_tag_suggestions(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetGroupTagSuggestions
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/GetGroupTagSuggestions/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_joined_groups_for_current_member(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetJoinedGroupsForCurrentMember
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/MyGroups/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_joined_groups_for_current_member_v2(self, currentPage):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetJoinedGroupsForCurrentMemberV2
        Access:   Method: GET
        :param currentPage: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/MyGroups/V2/" + currentPage + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_joined_groups_for_member(self, membershipId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetJoinedGroupsForMember
        Access:   Method: GET
        :param membershipId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/User/" + membershipId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_joined_groups_for_member_v2(self, currentPage, membershipId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetJoinedGroupsForMemberV2
        Access:   Method: GET
        :param currentPage: 
        :param membershipId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/User/" + membershipId + "/Joined/" + currentPage + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_joined_groups_for_member_v3(self, currentPage, membershipId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetJoinedGroupsForMemberV3
        Access: Public  Method: GET
        :param currentPage: 
        :param membershipId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/User/" + membershipId + "/JoinedV3/" + currentPage + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_members_of_clan(self, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetMembersOfClan
        Access: Public  Method: GET
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/ClanMembers/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_members_of_group(self, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetMembersOfGroup
        Access:   Method: GET
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_members_of_group_v2(self, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetMembersOfGroupV2
        Access:   Method: GET
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/MembersV2/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_members_of_group_v3(self, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetMembersOfGroupV3
        Access: Public  Method: GET
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/MembersV3/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_my_clan_memberships(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetMyClanMemberships
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/MyClans/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_pending_clan_memberships(self, groupId, currentPage, clanMembershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetPendingClanMemberships
        Access: Private  Method: GET
        :param groupId: 
        :param currentPage: 
        :param clanMembershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Clan/" + clanMembershipType + "/Pending/" + currentPage + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_pending_groups_for_current_member(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetPendingGroupsForCurrentMember
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/MyPendingGroups/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_pending_groups_for_current_member_v2(self, currentPage):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetPendingGroupsForCurrentMemberV2
        Access:   Method: GET
        :param currentPage: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/MyPendingGroups/V2/" + currentPage + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_pending_groups_for_member(self, membershipId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetPendingGroupsForMember
        Access:   Method: GET
        :param membershipId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/User/" + membershipId + "/Pending/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_pending_groups_for_member_v2(self, currentPage, membershipId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetPendingGroupsForMemberV2
        Access:   Method: GET
        :param currentPage: 
        :param membershipId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/User/" + membershipId + "/PendingV2/" + currentPage + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_pending_memberships(self, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetPendingMemberships
        Access:   Method: GET
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/Pending/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_pending_memberships_v2(self, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetPendingMembershipsV2
        Access: Private  Method: GET
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/PendingV2/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_recommended_groups(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GetRecommendedGroups
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/Recommended/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def group_search(self, access_token, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/GroupSearch
        Access: Public  Method: POST
        KWARGS values should be "param=value"
        :param contents.searchType: 
        :param creationDate: 
        :param itemsPerPage: 
        :param sortBy: 
        :param membershipType: 
        :param contents.searchValue: 
        :param tagText: 
        :param currentPage: 
        :param groupMemberCountFilter: 
        :param localeFilter: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/Search/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def invite_clan_member(self, access_token, groupId, membershipId, clanMembershipType, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/InviteClanMember
        Access: Private  Method: POST
        :param groupId: 
        :param membershipId: 
        :param clanMembershipType: 
        KWARGS values should be "param=value"
        :param title: 
        :param message: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/InviteToClan/" + membershipId + "/" + clanMembershipType + "/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def invite_group_member(self, access_token, groupId, membershipId, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/InviteGroupMember
        Access: Private  Method: POST
        :param groupId: 
        :param membershipId: 
        KWARGS values should be "param=value"
        :param title: 
        :param message: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Invite/" + membershipId + "/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def invite_many_to_join_alliance(self, access_token, groupId, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/InviteManyToJoinAlliance
        Access: Private  Method: POST
        :param groupId: 
        KWARGS values should be "param=value"
        :param messageContent.message: 
        :param targetIds: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Allies/InviteMany/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def invite_to_join_alliance(self, access_token, groupId, allyGroupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/InviteToJoinAlliance
        Access: Private  Method: POST
        :param groupId: 
        :param allyGroupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Allies/Invite/" + allyGroupId + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def join_clan_for_group(self, access_token, groupId, clanMembershipType, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/JoinClanForGroup
        Access: Private  Method: POST
        :param groupId: 
        :param clanMembershipType: 
        KWARGS values should be "param=value"
        :param message: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Clans/Join/" + clanMembershipType + "/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def kick_member(self, access_token, groupId, membershipId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/KickMember
        Access: Private  Method: POST
        :param groupId: 
        :param membershipId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/" + membershipId + "/Kick/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def leave_clan_for_group(self, access_token, groupId, clanMembershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/LeaveClanForGroup
        Access: Private  Method: POST
        :param groupId: 
        :param clanMembershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Clans/Leave/" + clanMembershipType + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def override_founder_admin(self, access_token, groupId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/OverrideFounderAdmin
        Access: Private  Method: POST
        :param groupId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Admin/FounderOverride/" + membershipType + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def refresh_clan_settings_in_destiny(self, access_token, clanMembershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/RefreshClanSettingsInDestiny
        Access: Private  Method: POST
        :param clanMembershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/MyClans/Refresh/" + clanMembershipType + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def request_group_membership(self, access_token, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/RequestGroupMembership
        Access: Private  Method: POST
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/Apply/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def request_group_membership_v2(self, access_token, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/RequestGroupMembershipV2
        Access: Private  Method: POST
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/ApplyV2/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def request_to_join_alliance(self, access_token, groupId, allyGroupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/RequestToJoinAlliance
        Access: Private  Method: POST
        :param groupId: 
        :param allyGroupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Allies/RequestToJoin/" + allyGroupId + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def rescind_group_membership(self, access_token, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/RescindGroupMembership
        Access: Private  Method: POST
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/Rescind/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def save_migration_selection(self, access_token, param3, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/SaveMigrationSelection
        Access: Private  Method: POST
        :param param3: 
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + param1 + "/MigrationSelection/" + param2 + "/" + param3 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def set_group_as_alliance(self, access_token, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/SetGroupAsAlliance
        Access: Private  Method: POST
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/SetAsAlliance/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def set_privacy(self, access_token, groupId, param2):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/SetPrivacy
        Access: Private  Method: POST
        :param groupId: 
        :param param2: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Privacy/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def unban_member(self, access_token, groupId, membershipId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/UnbanMember
        Access: Private  Method: POST
        :param groupId: 
        :param membershipId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Members/" + membershipId + "/Unban/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def undelete_group(self, access_token, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/UndeleteGroup
        Access: Private  Method: POST
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Undelete/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def unfollow_all_groups_with_group(self, access_token, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/UnfollowAllGroupsWithGroup
        Access: Private  Method: POST
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/UnfollowAll/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def unfollow_groups_with_group(self, access_token, groupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/UnfollowGroupsWithGroup
        Access: Private  Method: POST
        :param groupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/UnfollowList/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def unfollow_group_with_group(self, access_token, groupId, followGroupId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GroupService/UnfollowGroupWithGroup
        Access: Private  Method: POST
        :param groupId: 
        :param followGroupId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Group/" + groupId + "/Unfollow/" + followGroupId + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json


class CommunitycontentService(object):
    def __init__(self):
        pass

    def admin_set_community_live_member_ban_status(self, access_token, param3, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CommunitycontentService/AdminSetCommunityLiveMemberBanStatus
        Access: Private  Method: POST
        :param param3: 
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/CommunityContent/Live/Partnerships/" + param1 + "/" + param2 + "/Ban/" + param3 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def admin_set_community_live_member_feature_status(self, access_token, param3, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CommunitycontentService/AdminSetCommunityLiveMemberFeatureStatus
        Access: Private  Method: POST
        :param param3: 
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/CommunityContent/Live/Partnerships/" + param1 + "/" + param2 + "/Feature/" + param3 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def alter_approval_state(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CommunitycontentService/AlterApprovalState
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/CommunityContent/AlterApprovalState/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def edit_content(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CommunitycontentService/EditContent
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/CommunityContent/Edit/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_admin_community_live_statuses(self, param3, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CommunitycontentService/GetAdminCommunityLiveStatuses
        Access:   Method: GET
        :param param3: 
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/CommunityContent/Live/Admin/" + param1 + "/" + param2 + "/" + param3 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_approval_queue(self, param3, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CommunitycontentService/GetApprovalQueue
        Access:   Method: GET
        :param param3: 
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/CommunityContent/Queue/" + param1 + "/" + param2 + "/" + param3 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_community_content(self, param3, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CommunitycontentService/GetCommunityContent
        Access:   Method: GET
        :param param3: 
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/CommunityContent/Get/" + param1 + "/" + param2 + "/" + param3 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_community_featured_activity_modes(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CommunitycontentService/GetCommunityFeaturedActivityModes
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/CommunityContent/Live/ActivityModes/Featured/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_community_live_statuses(self, partnershipType, communityStatusSort, page):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CommunitycontentService/GetCommunityLiveStatuses
        Access:   Method: GET
        :param partnershipType: 
        :param communityStatusSort: 
        :param page: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/CommunityContent/Live/All/" + partnershipType + "/" + communityStatusSort + "/" + page + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_community_live_statuses_for_clanmates(self, partnershipType, communityStatusSort, page):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CommunitycontentService/GetCommunityLiveStatusesForClanmates
        Access:   Method: GET
        :param partnershipType: 
        :param communityStatusSort: 
        :param page: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/CommunityContent/Live/Clan/" + partnershipType + "/" + communityStatusSort + "/" + page + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_community_live_statuses_for_friends(self, partnershipType, communityStatusSort, page):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CommunitycontentService/GetCommunityLiveStatusesForFriends
        Access:   Method: GET
        :param partnershipType: 
        :param communityStatusSort: 
        :param page: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/CommunityContent/Live/Friends/" + partnershipType + "/" + communityStatusSort + "/" + page + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_featured_community_live_statuses(self, partnershipType, communityStatusSort, page):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CommunitycontentService/GetFeaturedCommunityLiveStatuses
        Access:   Method: GET
        :param partnershipType: 
        :param communityStatusSort: 
        :param page: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/CommunityContent/Live/Featured/" + partnershipType + "/" + communityStatusSort + "/" + page + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_streaming_status_for_member(self, membershipId, partnershipType, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CommunitycontentService/GetStreamingStatusForMember
        Access:   Method: GET
        :param membershipId: 
        :param partnershipType: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/CommunityContent/Live/Users/" + partnershipType + "/" + membershipType + "/" + membershipId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def submit_content(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CommunitycontentService/SubmitContent
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/CommunityContent/Submit/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json


class TokensService(object):
    def __init__(self):
        pass

    def apply_offer_to_current_destiny_membership(self, access_token, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TokensService/ApplyOfferToCurrentDestinyMembership
        Access: Private  Method: POST
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Tokens/ApplyOfferToCurrentDestinyMembership/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def break_bond(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TokensService/BreakBond
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Tokens/RAF/BreakBond/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def claim_and_apply_on_token(self, access_token, tokenType, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TokensService/ClaimAndApplyOnToken
        Access: Private  Method: POST
        :param tokenType: 
        KWARGS values should be "param=value"
        :param redeemCode: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Tokens/ClaimAndApplyToken/" + tokenType + "/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def claim_token(self, access_token, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TokensService/ClaimToken
        Access: Private  Method: POST
        KWARGS values should be "param=value"
        :param redeemCode: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Tokens/Claim/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def consume_marketplace_platform_code_offer(self, access_token, param3, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TokensService/ConsumeMarketplacePlatformCodeOffer
        Access: Private  Method: POST
        :param param3: 
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Tokens/ConsumeMarketplacePlatformCodeOffer/" + param1 + "/" + param2 + "/" + param3 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_current_user_offer_history(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TokensService/GetCurrentUserOfferHistory
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Tokens/OfferHistory/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_current_user_throttle_state(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TokensService/GetCurrentUserThrottleState
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Tokens/ThrottleState/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_raf_eligibility(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TokensService/GetRAFEligibility
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Tokens/RAF/GetEligibility/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def marketplace_platform_code_offer_history(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TokensService/MarketplacePlatformCodeOfferHistory
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Tokens/MarketplacePlatformCodeOfferHistory/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def raf_claim(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TokensService/RAFClaim
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Tokens/RAF/Claim/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def raf_generate_referral_code(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TokensService/RAFGenerateReferralCode
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Tokens/RAF/GenerateReferralCode/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def raf_get_new_player_bond_details(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TokensService/RAFGetNewPlayerBondDetails
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Tokens/RAF/GetNewPlayerBondDetails/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def raf_get_veteran_bond_details(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TokensService/RAFGetVeteranBondDetails
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Tokens/RAF/GetVeteranBondDetails/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def verify_age(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TokensService/VerifyAge
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Tokens/VerifyAge/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json


class MessageService(object):
    def __init__(self):
        pass

    def create_conversation(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/CreateConversation
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/CreateConversation/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def create_conversation_v2(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/CreateConversationV2
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/CreateConversationV2/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_alliance_invited_to_join_invitations(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetAllianceInvitedToJoinInvitations
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/AllianceInvitations/InvitationsToJoinAnotherGroup/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_alliance_join_invitations(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetAllianceJoinInvitations
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/AllianceInvitations/RequestsToJoinYourGroup/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_conversation_by_id(self, conversationId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetConversationById
        Access:   Method: GET
        :param conversationId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetConversationById/" + conversationId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_conversation_by_id_v2(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetConversationByIdV2
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetConversationByIdV2/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_conversations_v2(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetConversationsV2
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetConversationsV2/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_conversations_v3(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetConversationsV3
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetConversationsV3/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_conversations_v4(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetConversationsV4
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetConversationsV4/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_conversations_v5(self, currentPage):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetConversationsV5
        Access: Private  Method: GET
        :param currentPage: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetConversationsV5/" + currentPage + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_conversation_thread_v2(self, param3, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetConversationThreadV2
        Access:   Method: GET
        :param param3: 
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetConversationThreadV2/" + param1 + "/" + param2 + "/" + param3 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_conversation_thread_v3(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetConversationThreadV3
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetConversationThreadV3/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_conversation_with_member_id(self, memberId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetConversationWithMemberId
        Access:   Method: GET
        :param memberId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetConversationWithMember/" + memberId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_conversation_with_member_id_v2(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetConversationWithMemberIdV2
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetConversationWithMemberV2/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_group_conversations(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetGroupConversations
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetGroupConversations/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_invitation_details(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetInvitationDetails
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/Invitations/" + param1 + "/Details/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_total_conversation_count(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetTotalConversationCount
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetTotalConversationCount/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_unread_conversation_count_v2(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetUnreadConversationCountV2
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetUnreadPrivateConversationCount/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_unread_conversation_count_v3(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetUnreadConversationCountV3
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetUnreadConversationCountV3/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_unread_conversation_count_v4(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetUnreadConversationCountV4
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetUnreadConversationCountV4/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_unread_group_conversation_count(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/GetUnreadGroupConversationCount
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/GetUnreadGroupConversationCount/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def leave_conversation(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/LeaveConversation
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/LeaveConversation/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def moderate_group_wall(self, access_token, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/ModerateGroupWall
        Access: Private  Method: POST
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/ModerateGroupWall/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def review_all_invitations(self, access_token, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/ReviewAllInvitations
        Access: Private  Method: POST
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/Invitations/ReviewAllDirect/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def review_invitation(self, access_token, param3, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/ReviewInvitation
        Access: Private  Method: POST
        :param param3: 
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/Invitations/" + param1 + "/" + param2 + "/" + param3 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def review_invitation_direct(self, access_token, invitationId, invitationResponseState):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/ReviewInvitationDirect
        Access: Private  Method: POST
        :param invitationId: 
        :param invitationResponseState: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/Invitations/ReviewDirect/" + invitationId + "/" + invitationResponseState + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def review_invitations(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/ReviewInvitations
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/Invitations/ReviewListDirect/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def save_message_v2(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/SaveMessageV2
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/SaveMessageV2/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def save_message_v3(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/SaveMessageV3
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/SaveMessageV3/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def save_message_v4(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/SaveMessageV4
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/SaveMessageV4/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def update_conversation_last_viewed_timestamp(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/UpdateConversationLastViewedTimestamp
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/Conversations/UpdateLastViewedTimestamp/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def user_is_typing(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/MessageService/UserIsTyping
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Message/UserIsTyping/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json


class ActivityService(object):
    def __init__(self):
        pass

    def follow_tag(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/FollowTag
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/Tag/Follow/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def follow_user(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/FollowUser
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/User/" + param1 + "/Follow/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_application_activity_for_user(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetApplicationActivityForUser
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/User/" + param1 + "/Activities/Application/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_entities_followed_by_current_user(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetEntitiesFollowedByCurrentUser
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/Following/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_entities_followed_by_current_user_v2(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetEntitiesFollowedByCurrentUserV2
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/Following/V2/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_entities_followed_by_user(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetEntitiesFollowedByUser
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/User/" + param1 + "/Following/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_entities_followed_by_user_v2(self, param3, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetEntitiesFollowedByUserV2
        Access:   Method: GET
        :param param3: 
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/User/" + param1 + "/Following/V2/" + param2 + "/" + param3 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_followers_of_tag(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetFollowersOfTag
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/Tag/Followers/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_followers_of_user(self, profileId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetFollowersOfUser
        Access: Public  Method: GET
        :param profileId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/User/" + profileId + "/Followers/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_forum_activity_for_user(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetForumActivityForUser
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/User/" + param1 + "/Activities/Forums/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_forum_activity_for_user_v2(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetForumActivityForUserV2
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/User/" + param1 + "/Activities/ForumsV2/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_friends(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetFriends
        Access: Public  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/Friends/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_friends_all_no_presence(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetFriendsAllNoPresence
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/Friends/AllNoPresence/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_friends_paged(self, currentPage, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetFriendsPaged
        Access: Private  Method: GET
        :param currentPage: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/Friends/Paged/" + membershipType + "/" + currentPage + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_groups_followed_by_current_user(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetGroupsFollowedByCurrentUser
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/Following/Groups/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_groups_followed_by_user(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetGroupsFollowedByUser
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/User/" + param1 + "/Following/Groups/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_groups_followed_paged_by_current_user(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetGroupsFollowedPagedByCurrentUser
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/Following/Groups/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_groups_followed_paged_by_user(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetGroupsFollowedPagedByUser
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/User/" + param1 + "/Following/Groups/Paged/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_like_and_share_activity_for_user(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetLikeAndShareActivityForUser
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/User/" + param1 + "/Activities/LikesAndShares/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_like_and_share_activity_for_user_v2(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetLikeAndShareActivityForUserV2
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/User/" + param1 + "/Activities/LikesAndSharesV2/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_like_share_and_forum_activity_for_user(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetLikeShareAndForumActivityForUser
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/User/" + param1 + "/Activities/LikeShareAndForum/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_users_followed_by_current_user(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/GetUsersFollowedByCurrentUser
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/Following/Users/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def unfollow_tag(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/UnfollowTag
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/Tag/Unfollow/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def unfollow_user(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ActivityService/UnfollowUser
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Activity/User/" + param1 + "/Unfollow/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json


class JSONPService(object):
    def __init__(self):
        pass

    def get_current_user(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/JSONPService/GetCurrentUser
        Access: Private  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/JSONP/GetBungieNetUser/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json


class IgnoreService(object):
    def __init__(self):
        pass

    def flag_item(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/IgnoreService/FlagItem
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Ignore/Flag/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_ignores_for_user(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/IgnoreService/GetIgnoresForUser
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Ignore/MyIgnores/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_ignore_status_for_post(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/IgnoreService/GetIgnoreStatusForPost
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Ignore/MyIgnores/Posts/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_ignore_status_for_user(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/IgnoreService/GetIgnoreStatusForUser
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Ignore/MyIgnores/Users/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_report_context(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/IgnoreService/GetReportContext
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Ignore/ReportContext/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def ignore_item(self, access_token, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/IgnoreService/IgnoreItem
        Access: Private  Method: POST
        KWARGS values should be "param=value"
        :param itemContextType: 
        :param ignoredItemId: 
        :param reason: 
        :param comment: 
        :param itemContextId: 
        :param ModeratorRequest: 
        :param ignoredItemType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Ignore/Ignore/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def my_last_report(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/IgnoreService/MyLastReport
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Ignore/MyLastReport/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def unignore_item(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/IgnoreService/UnignoreItem
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Ignore/Unignore/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json


class TrendingService(object):
    def __init__(self):
        pass

    def get_trending_categories(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TrendingService/GetTrendingCategories
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Trending/Categories/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_trending_category(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TrendingService/GetTrendingCategory
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Trending/Categories/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_trending_entry_detail(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/TrendingService/GetTrendingEntryDetail
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Trending/Details/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json


class CoreService(object):
    def __init__(self):
        pass

    def get_available_locales(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CoreService/GetAvailableLocales
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform//GetAvailableLocales/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_common_settings(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CoreService/GetCommonSettings
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform//Settings/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_global_alerts(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CoreService/GetGlobalAlerts
        Access: Public  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform//GlobalAlerts/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_system_status(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CoreService/GetSystemStatus
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform//Status/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def hello_world(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/CoreService/HelloWorld
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform//HelloWorld/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json


class DestinyService(object):
    def __init__(self):
        pass

    def equip_item(self, access_token, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/EquipItem
        Access: Private  Method: POST
        KWARGS values should be "param=value"
        :param itemId: 
        :param characterId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/EquipItem/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def equip_items(self, access_token, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/EquipItems
        Access: Private  Method: POST
        KWARGS values should be "param=value"
        :param characterId: 
        :param itemIds: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/EquipItems/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_account(self, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetAccount
        Access: Public  Method: GET
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Account/" + destinyMembershipId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_account_summary(self, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetAccountSummary
        Access:   Method: GET
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Account/" + destinyMembershipId + "/Summary/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_activity_blob(self, e):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetActivityBlob
        Access:   Method: GET
        :param e: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Stats/ActivityBlob/" + e + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_activity_history(self, characterId, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetActivityHistory
        Access: Public  Method: GET
        :param characterId: 
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Stats/ActivityHistory/" + membershipType + "/" + destinyMembershipId + "/" + characterId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_advisors_for_account(self, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetAdvisorsForAccount
        Access:   Method: GET
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Account/" + destinyMembershipId + "/Advisors/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_advisors_for_character(self, characterId, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetAdvisorsForCharacter
        Access: Public  Method: GET
        :param characterId: 
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Account/" + destinyMembershipId + "/Character/" + characterId + "/Advisors/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_advisors_for_character_v2(self, characterId, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetAdvisorsForCharacterV2
        Access:   Method: GET
        :param characterId: 
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Account/" + destinyMembershipId + "/Character/" + characterId + "/Advisors/V2/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_advisors_for_current_character(self, characterId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetAdvisorsForCurrentCharacter
        Access: Private  Method: GET
        :param characterId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/MyAccount/Character/" + characterId + "/Advisors/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_all_items_summary(self, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetAllItemsSummary
        Access: Public  Method: GET
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Account/" + destinyMembershipId + "/Items/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_all_vendors_for_current_character(self, characterId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetAllVendorsForCurrentCharacter
        Access:   Method: GET
        :param characterId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/MyAccount/Character/" + characterId + "/Vendors/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_bond_advisors(self, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetBondAdvisors
        Access:   Method: GET
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/MyAccount/Advisors/Bonds/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_character(self, characterId, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetCharacter
        Access: Private  Method: GET
        :param characterId: 
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Account/" + destinyMembershipId + "/Character/" + characterId + "/Complete/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_character_activities(self, characterId, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetCharacterActivities
        Access: Public  Method: GET
        :param characterId: 
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Account/" + destinyMembershipId + "/Character/" + characterId + "/Activities/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_character_inventory(self, characterId, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetCharacterInventory
        Access: Public  Method: GET
        :param characterId: 
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Account/" + destinyMembershipId + "/Character/" + characterId + "/Inventory/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_character_inventory_summary(self, characterId, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetCharacterInventorySummary
        Access:   Method: GET
        :param characterId: 
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Account/" + destinyMembershipId + "/Character/" + characterId + "/Inventory/Summary/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_character_progression(self, characterId, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetCharacterProgression
        Access: Public  Method: GET
        :param characterId: 
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Account/" + destinyMembershipId + "/Character/" + characterId + "/Progression/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_character_summary(self, characterId, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetCharacterSummary
        Access: Public  Method: GET
        :param characterId: 
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Account/" + destinyMembershipId + "/Character/" + characterId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_clan_leaderboards(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetClanLeaderboards
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Stats/ClanLeaderboards/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_destiny_aggregate_activity_stats(self, characterId, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetDestinyAggregateActivityStats
        Access: Public  Method: GET
        :param characterId: 
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Stats/AggregateActivityStats/" + membershipType + "/" + destinyMembershipId + "/" + characterId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_destiny_explorer_items(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetDestinyExplorerItems
        Access: Public  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Explorer/Items/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_destiny_explorer_talent_node_steps(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetDestinyExplorerTalentNodeSteps
        Access: Public  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Explorer/TalentNodeSteps/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_destiny_live_tile_content_items(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetDestinyLiveTileContentItems
        Access: Public  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/LiveTiles/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_destiny_manifest(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetDestinyManifest
        Access: Public  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Manifest/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_destiny_single_definition(self, definitionId, definitionType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetDestinySingleDefinition
        Access: Public  Method: GET
        :param definitionId: 
        :param definitionType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Manifest/" + definitionType + "/" + definitionId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_excellence_badges(self, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetExcellenceBadges
        Access: Public  Method: GET
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Stats/GetExcellenceBadges/" + membershipType + "/" + destinyMembershipId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_grimoire_by_membership(self, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetGrimoireByMembership
        Access: Public  Method: GET
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Vanguard/Grimoire/" + membershipType + "/" + destinyMembershipId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_grimoire_definition(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetGrimoireDefinition
        Access: Public  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Vanguard/Grimoire/Definition/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_historical_stats(self, characterId, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetHistoricalStats
        Access: Public  Method: GET
        :param characterId: 
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Stats/" + membershipType + "/" + destinyMembershipId + "/" + characterId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_historical_stats_definition(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetHistoricalStatsDefinition
        Access: Public  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Stats/Definition/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_historical_stats_for_account(self, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetHistoricalStatsForAccount
        Access: Public  Method: GET
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Stats/Account/" + membershipType + "/" + destinyMembershipId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_item_detail(self, characterId, destinyMembershipId, itemInstanceId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetItemDetail
        Access: Public  Method: GET
        :param characterId: 
        :param destinyMembershipId: 
        :param itemInstanceId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Account/" + destinyMembershipId + "/Character/" + characterId + "/Inventory/" + itemInstanceId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_item_reference_detail(self, param3, param2, param1, param4):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetItemReferenceDetail
        Access:   Method: GET
        :param param3: 
        :param param2: 
        :param param1: 
        :param param4: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + param1 + "/Account/" + param2 + "/Character/" + param3 + "/ItemReference/" + param4 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_leaderboards(self, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetLeaderboards
        Access: Private  Method: GET
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Stats/Leaderboards/" + membershipType + "/" + destinyMembershipId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_leaderboards_for_character(self, characterId, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetLeaderboardsForCharacter
        Access: Private  Method: GET
        :param characterId: 
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Stats/Leaderboards/" + membershipType + "/" + destinyMembershipId + "/" + characterId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_leaderboards_for_psn(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetLeaderboardsForPsn
        Access: Private  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Stats/LeaderboardsForPsn/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_membership_id_by_display_name(self, membershipType, displayName):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetMembershipIdByDisplayName
        Access: Public  Method: GET
        :param membershipType: 
        :param displayName: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Stats/GetMembershipIdByDisplayName/" + displayName + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_my_grimoire(self, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetMyGrimoire
        Access: Private  Method: GET
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Vanguard/Grimoire/" + membershipType + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_post_game_carnage_report(self, activityInstanceId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetPostGameCarnageReport
        Access: Public  Method: GET
        :param activityInstanceId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Stats/PostGameCarnageReport/" + activityInstanceId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_public_advisors(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetPublicAdvisors
        Access: Public  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Advisors/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_public_advisors_v2(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetPublicAdvisorsV2
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Advisors/V2/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_public_vendor(self, vendorId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetPublicVendor
        Access: Public  Method: GET
        :param vendorId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Vendors/" + vendorId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_public_vendor_with_metadata(self, vendorId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetPublicVendorWithMetadata
        Access: Public  Method: GET
        :param vendorId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Vendors/" + vendorId + "/Metadata/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_public_xur_vendor(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetPublicXurVendor
        Access: Public  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Advisors/Xur/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_record_book_completion_status(self, membershipType, recordBookHash):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetRecordBookCompletionStatus
        Access: Private  Method: GET
        :param membershipType: 
        :param recordBookHash: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/MyAccount/RecordBooks/" + recordBookHash + "/Completion/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_special_event_advisors(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetSpecialEventAdvisors
        Access: Public  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Events/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_triumphs(self, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetTriumphs
        Access: Public  Method: GET
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/Account/" + destinyMembershipId + "/Triumphs/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_unique_weapon_history(self, characterId, destinyMembershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetUniqueWeaponHistory
        Access: Public  Method: GET
        :param characterId: 
        :param destinyMembershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/Stats/UniqueWeapons/" + membershipType + "/" + destinyMembershipId + "/" + characterId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_vault(self, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetVault
        Access: Private  Method: GET
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/MyAccount/Vault/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_vault_summary(self, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetVaultSummary
        Access:   Method: GET
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/MyAccount/Vault/Summary/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_vendor_for_current_character(self, characterId, vendorId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetVendorForCurrentCharacter
        Access: Private  Method: GET
        :param characterId: 
        :param vendorId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/MyAccount/Character/" + characterId + "/Vendor/" + vendorId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_vendor_for_current_character_with_metadata(self, characterId, vendorId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetVendorForCurrentCharacterWithMetadata
        Access: Private  Method: GET
        :param characterId: 
        :param vendorId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/MyAccount/Character/" + characterId + "/Vendor/" + vendorId + "/Metadata/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_vendor_item_detail_for_current_character(self, characterId, itemId, vendorId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetVendorItemDetailForCurrentCharacter
        Access: Private  Method: GET
        :param characterId: 
        :param itemId: 
        :param vendorId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/MyAccount/Character/" + characterId + "/Vendor/" + vendorId + "/Item/" + itemId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_vendor_item_detail_for_current_character_with_metadata(self, characterId, itemId, vendorId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetVendorItemDetailForCurrentCharacterWithMetadata
        Access: Private  Method: GET
        :param characterId: 
        :param itemId: 
        :param vendorId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/MyAccount/Character/" + characterId + "/Vendor/" + vendorId + "/Item/" + itemId + "/Metadata/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_vendor_summaries_for_current_character(self, characterId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/GetVendorSummariesForCurrentCharacter
        Access: Private  Method: GET
        :param characterId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/" + membershipType + "/MyAccount/Character/" + characterId + "/Vendors/Summaries/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def search_destiny_player(self, membershipType, displayName):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/SearchDestinyPlayer
        Access: Public  Method: GET
        :param membershipType: 
        :param displayName: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/SearchDestinyPlayer/" + membershipType + "/" + displayName + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def set_item_lock_state(self, access_token, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/SetItemLockState
        Access: Private  Method: POST
        KWARGS values should be "param=value"
        :param itemId: 
        :param characterId: 
        :param state: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/SetLockState/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def set_quest_tracked_state(self, access_token, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/SetQuestTrackedState
        Access: Private  Method: POST
        KWARGS values should be "param=value"
        :param characterId: 
        :param itemId: 
        :param membershipId: 
        :param membershipType: 
        :param state: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/SetQuestTrackedState/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def transfer_item(self, access_token, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/DestinyService/TransferItem
        Access: Private  Method: POST
        KWARGS values should be "param=value"
        :param itemId: 
        :param characterId: 
        :param itemReferenceHash: 
        :param transferToVault: 
        :param membershipType: 
        :param stackSize: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/d1/Platform/Destiny/TransferItem/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json


class NotificationService(object):
    def __init__(self):
        pass

    def get_real_time_events(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/NotificationService/GetRealTimeEvents
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Notification/Events/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_recent_notification_count(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/NotificationService/GetRecentNotificationCount
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Notification/GetCount/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_recent_notifications(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/NotificationService/GetRecentNotifications
        Access: Private  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Notification/GetRecent/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def reset_notification(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/NotificationService/ResetNotification
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Notification/Reset/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json


class UserService(object):
    def __init__(self):
        pass

    def create_user(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/CreateUser
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/CreateUser/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def edit_success_message_flags(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/EditSuccessMessageFlags
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/MessageFlags/Success/Update/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_available_avatars(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetAvailableAvatars
        Access: Private  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetAvailableAvatars/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_available_avatars_admin(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetAvailableAvatarsAdmin
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetAvailableAvatarsAdmin/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_available_themes(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetAvailableThemes
        Access: Public  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetAvailableThemes/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_bungie_account(self, membershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetBungieAccount
        Access: Public  Method: GET
        :param membershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetBungieAccount/" + membershipId + "/" + membershipType + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_bungie_net_user_by_id(self, membershipId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetBungieNetUserById
        Access:   Method: GET
        :param membershipId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetBungieNetUserById/" + membershipId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_counts_for_current_user(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetCountsForCurrentUser
        Access: Private  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetCounts/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_credential_types_for_account(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetCredentialTypesForAccount
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetCredentialTypesForAccount/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_current_bungie_account(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetCurrentBungieAccount
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetCurrentBungieAccount/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_current_bungie_net_user(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetCurrentBungieNetUser
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetCurrentBungieNetUser/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_current_user(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetCurrentUser-(User)
        Access: Private  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetBungieNetUser/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_membership_data_by_id(self, membershipId, membershipType):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetMembershipDataById
        Access:   Method: GET
        :param membershipId: 
        :param membershipType: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetMembershipsById/" + membershipId + "/" + membershipType + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_membership_data_for_current_user(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetMembershipDataForCurrentUser
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetMembershipsForCurrentUser/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_mobile_app_pairings(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetMobileAppPairings
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetMobileAppPairings/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_mobile_app_pairings_uncached(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetMobileAppPairingsUncached
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetMobileAppPairingsUncached/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_notification_settings(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetNotificationSettings
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetNotificationSettings/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_partnerships(self, membershipId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetPartnerships
        Access:   Method: GET
        :param membershipId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/" + membershipId + "/Partnerships/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_platform_api_keys_for_user(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetPlatformApiKeysForUser
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetPlatformApiKeysForUser/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_sign_out_url(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetSignOutUrl
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetSignOutUrl/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_user_aliases(self, membershipId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetUserAliases
        Access:   Method: GET
        :param membershipId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetUserAliases/" + membershipId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_user_membership_ids(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/GetUserMembershipIds
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/GetMembershipIds/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def link_override(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/LinkOverride
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/LinkOverride/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def register_mobile_app_pair(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/RegisterMobileAppPair
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/RegisterMobileAppPair/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def remove_partnership(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/RemovePartnership
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/Partnerships/" + param1 + "/Remove/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def search_users(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/SearchUsers
        Access: Public  Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/SearchUsers/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def search_users_paged(self, page, searchTerm):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/SearchUsersPaged
        Access:   Method: GET
        :param page: 
        :param searchTerm: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/SearchUsersPaged/" + searchTerm + "/" + page + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def search_users_paged_v2(self, param3, page, searchTerm):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/SearchUsersPagedV2
        Access:   Method: GET
        :param param3: 
        :param page: 
        :param searchTerm: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/SearchUsersPaged/" + searchTerm + "/" + page + "/" + param3 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def set_acknowledged(self, access_token, ackId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/SetAcknowledged
        Access: Private  Method: POST
        :param ackId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/Acknowledged/" + ackId + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def unregister_mobile_app_pair(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/UnregisterMobileAppPair
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/UnregisterMobileAppPair/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def update_destiny_emblem_avatar(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/UpdateDestinyEmblemAvatar
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/UpdateDestinyEmblemAvatar/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def update_notification_setting(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/UpdateNotificationSetting
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/Notification/Update/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def update_state_info_for_mobile_app_pair(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/UpdateStateInfoForMobileAppPair
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/UpdateStateInfoForMobileAppPair/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def update_user(self, access_token, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/UpdateUser
        Access: Private  Method: POST
        KWARGS values should be "param=value"
        :param showGroupMessaging: 
        :param profilePicture: 
        :param showGamertagPublic: 
        :param emailAddress: 
        :param displayName: 
        :param adultMode: 
        :param profileTheme: 
        :param emailUsage: 
        :param uniqueName: 
        :param localeInheritDefault: 
        :param showActivity: 
        :param locale: 
        :param showPsnPublic: 
        :param showFacebookPublic: 
        :param about: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/UpdateUser/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def update_user_admin(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/UserService/UpdateUserAdmin
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/User/UpdateUserAdmin/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json


class SurveyService(object):
    def __init__(self):
        pass

    def get_survey(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/SurveyService/GetSurvey
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Survey/GetSurvey/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json


class GameService(object):
    def __init__(self):
        pass

    def get_player_games_by_id(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GameService/GetPlayerGamesById
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Game/GetPlayerGamesById/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def reach_model_sneaker_net(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/GameService/ReachModelSneakerNet
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Game/ReachModelSneakerNet/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json


class ForumService(object):
    def __init__(self):
        pass

    def approve_fireteam_thread(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/ApproveFireteamThread
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/Recruit/Approve/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def change_lock_state(self, access_token, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/ChangeLockState
        Access: Private  Method: POST
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/ChangeLockState/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def change_pin_state(self, access_token, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/ChangePinState
        Access: Private  Method: POST
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/ChangePinState/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def create_content_comment(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/CreateContentComment
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/CreateContentComment/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def create_post(self, access_token, **kwargs):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/CreatePost
        Access: Private  Method: POST
        KWARGS values should be "param=value"
        :param groupId: 
        :param urlLinkOrImage: 
        :param isGroupPrivate: 
        :param body: 
        :param subject: 
        :param category: 
        :param metadata: 
        :param parentPostId: 
        :param subTopicOverride: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/CreatePost/?**kwargs"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def delete_post(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/DeletePost
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/DeletePost/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def edit_post(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/EditPost
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/EditPost/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_core_topics_paged(self, param3, param2, param1, param4):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/GetCoreTopicsPaged
        Access:   Method: GET
        :param param3: 
        :param param2: 
        :param param1: 
        :param param4: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/GetCoreTopicsPaged/" + param1 + "/" + param2 + "/" + param3 + "/" + param4 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_forum_tag_count_estimate(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/GetForumTagCountEstimate
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/GetForumTagCountEstimate/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_forum_tag_suggestions(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/GetForumTagSuggestions
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/GetForumTagSuggestions/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_poll(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/GetPoll
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/Poll/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_popular_tags(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/GetPopularTags
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/GetPopularTags/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_post_and_parent(self, childPostId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/GetPostAndParent
        Access:   Method: GET
        :param childPostId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/GetPostAndParent/" + childPostId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_post_and_parent_awaiting_approval(self, childPostId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/GetPostAndParentAwaitingApproval
        Access:   Method: GET
        :param childPostId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/GetPostAndParentAwaitingApproval/" + childPostId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_posts_threaded_paged(self, sortMode, page, replySize, rootThreadMode, pageSize, parentPostId, getParentPost):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/GetPostsThreadedPaged
        Access:   Method: GET
        :param sortMode: 
        :param page: 
        :param replySize: 
        :param rootThreadMode: 
        :param pageSize: 
        :param parentPostId: 
        :param getParentPost: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/GetPostsThreadedPaged/" + parentPostId + "/" + page + "/" + pageSize + "/" + replySize + "/" + getParentPost + "/" + rootThreadMode + "/" + sortMode + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_posts_threaded_paged_from_child(self, sortMode, page, replySize, rootThreadMode, childPostId, pageSize):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/GetPostsThreadedPagedFromChild
        Access:   Method: GET
        :param sortMode: 
        :param page: 
        :param replySize: 
        :param rootThreadMode: 
        :param childPostId: 
        :param pageSize: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/GetPostsThreadedPagedFromChild/" + childPostId + "/" + page + "/" + pageSize + "/" + replySize + "/" + rootThreadMode + "/" + sortMode + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_recruitment_thread_summaries(self, access_token):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/GetRecruitmentThreadSummaries
        Access: Private  Method: POST
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/Recruit/Summaries/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def get_topic_for_content(self, contentId):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/GetTopicForContent
        Access:   Method: GET
        :param contentId: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/GetTopicForContent/" + contentId + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_topics_paged(self, page, categoryFilter, sort, quickDate, pageSize, group):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/GetTopicsPaged
        Access: Public  Method: GET
        :param page: 
        :param categoryFilter: 
        :param sort: 
        :param quickDate: 
        :param pageSize: 
        :param group: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/GetTopicsPaged/" + page + "/" + pageSize + "/" + group + "/" + sort + "/" + quickDate + "/" + categoryFilter + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def join_fireteam_thread(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/JoinFireteamThread
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/Recruit/Join/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def kick_ban_fireteam_applicant(self, access_token, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/KickBanFireteamApplicant
        Access: Private  Method: POST
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/Recruit/KickBan/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def leave_fireteam_thread(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/LeaveFireteamThread
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/Recruit/Leave/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def mark_reply_as_answer(self, access_token, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/MarkReplyAsAnswer
        Access: Private  Method: POST
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/MarkReplyAsAnswer/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def moderate_group_post(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/ModerateGroupPost
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/Post/" + param1 + "/GroupModerate/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def moderate_post(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/ModeratePost
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/Post/" + param1 + "/Moderate/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def moderate_tag(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/ModerateTag
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/Tags/" + param1 + "/Moderate/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def poll_vote(self, access_token, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/PollVote
        Access: Private  Method: POST
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/Poll/Vote/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def rate_post(self, access_token, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/RatePost
        Access: Private  Method: POST
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/RatePost/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def unmark_reply_as_answer(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ForumService/UnmarkReplyAsAnswer
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Forum/UnmarkReplyAsAnswer/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json


class ContentService(object):
    def __init__(self):
        pass

    def get_career(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/GetCareer
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/Careers/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_careers(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/GetCareers
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/Careers/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_content_by_id(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/GetContentById
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/GetContentById/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_content_by_tag_and_type(self, param3, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/GetContentByTagAndType
        Access:   Method: GET
        :param param3: 
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/GetContentByTagAndType/" + param1 + "/" + param2 + "/" + param3 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_content_type(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/GetContentType
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/GetContentType/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_destiny_content(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/GetDestinyContent
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/Site/Destiny/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_destiny_content_v2(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/GetDestinyContentV2
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/Site/Destiny/V2/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_featured_article(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/GetFeaturedArticle
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/Site/Featured/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_homepage_content(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/GetHomepageContent
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/Site/Homepage/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_homepage_content_v2(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/GetHomepageContentV2
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/Site/Homepage/V2/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_jobs(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/GetJobs
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/Site/Jobs/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_news(self, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/GetNews
        Access:   Method: GET
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/Site/News/" + param1 + "/" + param2 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_promo_widget(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/GetPromoWidget
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/Site/Destiny/Promo/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def get_publications(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/GetPublications
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/Site/Publications/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def search_careers(self):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/SearchCareers
        Access:   Method: GET
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/Careers/Search/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def search_content_by_tag_and_type(self, param3, param2, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/SearchContentByTagAndType
        Access:   Method: GET
        :param param3: 
        :param param2: 
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/SearchContentByTagAndType/" + param1 + "/" + param2 + "/" + param3 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json

    def search_content_ex(self, access_token, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/SearchContentEx
        Access: Private  Method: POST
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/SearchEx/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_private)
        this_json = r.json()
        return this_json

    def search_content_with_text(self, param1):
        """See https://destinydevs.github.io/BungieNetPlatform/docs/ContentService/SearchContentWithText
        Access:   Method: GET
        :param param1: 
        :return: Returns JSON
        :rtype: Dict
        """
        request_session = requests.session()
        url = "https://www.bungie.net/Platform/Content/Search/" + param1 + "/"
        r = request_session.get(url, headers=api_headers_public)
        this_json = r.json()
        return this_json
