import logging
import puremagic

from synapse.module_api import ModuleApi

logger = logging.getLogger(__name__)


class SynapseMediacheck(object):
    def __init__(self, config: dict, api: ModuleApi):
        self.config = config
        self.api = api
        self._media_path = config.get("media_path", "")
        self._allowed_mimetypes = config.get("allowed_mimetypes", [])

        self.api.register_spam_checker_callbacks(
            check_media_file_for_spam=self.check_media_file_for_spam,
        )

    async def check_media_file_for_spam(file_wrapper: "synapse.rest.media.v1.media_storage.ReadableFileWrapper",
                                        file_info: "synapse.rest.media.v1._base.FileInfo",
                                        ) -> bool:
        logger.info("check_media_file_for_spam - server_name: %s, file_id: %s, "
                    "url_cache: %s, thumbnail: %s, thumbnail_width: %s, thumbnail_height: %s, "
                    "thumbnail_method: %s, thumbnail_type: %s, thumbnail_length: %s",
                    "thumbnail_method: %s, thumbnail_type: %s, thumbnail_length: %s",
                    "thumbnail_method: %s, thumbnail_type: %s, thumbnail_length: %s",
                    file_info.server_name, file_info.file_id,
                    file_info.server_name, file_info.file_id,
                    file_info.server_name, file_info.file_id,
                    file_info.url_cache, file_info.thumbnail, file_info.thumbnail_width, file_info.thumbnail_height,
                    file_info.url_cache, file_info.thumbnail, file_info.thumbnail_width, file_info.thumbnail_height,
                    file_info.url_cache, file_info.thumbnail, file_info.thumbnail_width, file_info.thumbnail_height,
                    file_info.thumbnail_method, file_info.thumbnail_type, file_info.thumbnail_length)

        #logger.info("hs: %s hostname: %s", self.api._hs, self.api._hs.hostname)

        mime = ''
        if file_info.thumbnail:
            mime = file_info.thumbnail_type
        else:
            mime = puremagic.from_file(self._media_path + file_info.file_id[:2]
                                       + '/' + file_info.file_id[2:4] + '/' + file_info.file_id[4:], True)  # todo - get path from environment/config/api
        logger.info("mime: %s", mime)

        for m in self._allowed_mimetypes:
            if mime == m:
                return False  # allowed

        return True  # blocked

    @staticmethod
    def parse_config(config: dict):
        return config  # no parsing needed
