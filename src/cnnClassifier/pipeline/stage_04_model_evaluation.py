from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation import ModelEvaluation
from cnnClassifier import logger



STAGE_NAME = "Model Evaluation Stage"


class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = ModelEvaluation(config=eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        # evaluation.log_into_mlflow()
        
        
        

if __name__ == "__main__":
    try:
        logger.info(f"*****************")
        logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} Complted <<<<<\n\nX===============X")
    
    except Exception as e:
        logger.exception(e)
        raise e