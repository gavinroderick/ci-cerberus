from githubparsers import workflowparser
from utils.logging import setup_logger

logger = setup_logger(__name__)

if __name__ == '__main__':
    # nvd_client = NvdHttpClient("https://services.nvd.nist.gov/")
    # cves = nvd_client.find_cves_by_keywords("tj-actions")

    # logger.info(cves)
    parser = workflowparser.WorkflowParser()
    actions = parser.get_workflows()
    logger.info(actions)