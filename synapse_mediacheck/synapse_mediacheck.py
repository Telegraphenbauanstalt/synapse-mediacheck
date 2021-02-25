import logging

logger = logging.getLogger(__name__)
#logger = logging.getLogger("synapse_mediacheck")

class SynapseMediacheck(object):
    def __init__(self, config, api):
        self.config = config
        self.api = api
        logger.info("SynapseMediacheck initialized!")

    def check_event_for_spam(self, event):
        logger.info("check_event_for_spam %s, event_id:%s, content:%s", event, event.event_id, event.get("content", "") )
        return False  # allow all events

    def check_media_file_for_spam(self, file_wrapper, file_info):
        logger.info("check_media_file_for_spam - server_name: %s, file_id: %s, " \
        "url_cache: %s, thumbnail: %s, thumbnail_width: %s, thumbnail_height: %s, " \
        "thumbnail_method: %s, thumbnail_type: %s, thumbnail_length: %s", 
        file_info.server_name, file_info.file_id, 
        file_info.url_cache, file_info.thumbnail, file_info.thumbnail_width, file_info.thumbnail_height, 
        file_info.thumbnail_method, file_info.thumbnail_type, file_info.thumbnail_length )
        return False  # allow all media

        # I don't have a clue how to get the content-type of the uploaded media file,
        # perhaps MediaRepository https://github.com/matrix-org/synapse/blob/v1.28.0/synapse/rest/media/v1/media_repository.py 
        # could help?

    def user_may_invite(self, inviter_userid, invitee_userid, room_id):
        return True  # allow all invites

    def user_may_create_room(self, userid):
        return True  # allow all room creations

    def user_may_create_room_alias(self, userid, room_alias):
        return True  # allow all room aliases

    def user_may_publish_room(self, userid, room_id):
        return True  # allow publishing of all rooms

    def check_username_for_spam(self, user_profile):
        return False  # allow all usernames

    @staticmethod
    def parse_config(config):
        return config # no parsing needed
