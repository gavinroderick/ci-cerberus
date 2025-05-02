import argparse
import logging

from utils import log_utils

if __name__ == "__main__":

    # Find out how much the user wants to know
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--verbosity",
        "-v",
        default="INFO",
        choices=["DEBUG", "INFO"],
        help="Set output verbosity",
    )
    args = parser.parse_args()

    # Setup logging globally
    log_utils.setup_logger(verbosity=args.verbosity)
    logger = logging.getLogger(__name__)

    # Let's go!
    logger.info("Starting ci-cerberus")

    # nvd_client = NvdHttpClient("https://services.nvd.nist.gov/")
    # cves = nvd_client.find_cves_by_keywords("tj-actions")

    # logger.info(cves)
    # parser = workflowparser.WorkflowParser()
    # actions = parser.get_workflows()
    # logger.info(actions)
