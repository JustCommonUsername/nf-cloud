# external imports
from flask import request, jsonify

# internal imports
from nf_cloud_backend import app, get_database_connection, config


class NextflowWorkflowControllers:
    """
    Handles requests regarding the defined nextflow workflows
    """

    @staticmethod
    @app.route("/api/nextflow-workflows")
    def nextflow_workflows():
        """
        Returns
        -------
        JSON with keys 'local' and 'docker', both keys contained the list of workflow names.
        """
        return jsonify({
            "nextflow_workflows":{
                "local": sorted([
                    workflow
                    for workflow in config["workflows"]["local"].keys()
                ]),
                "docker": sorted([
                    workflow
                    for workflow in config["workflows"]["docker"].keys()
                ])
            }
        })

    @staticmethod
    @app.route("/api/nextflow-workflows/<string:nextflow_workflow_type>/<string:nextflow_workflow>/arguments")
    def arguments(nextflow_workflow_type: str, nextflow_workflow: str):
        """
        Returns
        -------
        JSON where each key is the name of a workflow argument with value type definition and description.
        """
        return jsonify({
            "arguments": config["workflows"][nextflow_workflow_type][nextflow_workflow]["args"]["dynamic"]
        })