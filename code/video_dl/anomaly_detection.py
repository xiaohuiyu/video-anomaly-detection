from anomaly_models import BetterAnomalyModel
import config

def change_phase_factory():
    loss_history = []
    classification_history = []

    def change_phase(loss, classification):
        loss_history.append(loss)
        classification_history.append(classification)

        #TODO: This is a stub
        return False

def is_anomaly(classification):
    #TODO: THis is a stub
    return False

def anomaly_detection_proc(frames_queue, conf):
    
    #1. Create the model
    seq_len = conf['model']['seq_len']
    gru_dropout = conf['model']['gru_dropout']
    output_dim = conf['model']['output_dim']
    model = BetterAnomalyModel(output_dim, gru_dropout, seq_len)
    change_phase = change_phase_factory()
    phase = "TRAINING"

    while True:
        message = frames_queue.get(True)
        if message == config.FINISH_SIGNAL:
            break
        _, frame = message

        #TODO: Pass the right target format here
        if phase == "TRAINING":
            loss, classification = model.loss(frame, [0, 1])
            if change_phase(loss, classification):
                phase = "DETECTION"
                print("NOW IN DETECTION PHASE")
        elif phase == "DETECTION":
            classification = model.forward(frame)
            if is_anomaly(classification):
                print("ANOMALY DETECTED")


        
            

    #2. while not finish_signal
    #2.1 Get frame from queue
    
    #2.2 if phase is TRAINING:
    #2.2.1 Submit frame for model training
    #2.2.2 Get back the results from training
    #2.2.3 Check history of results to see if phase changes
    
    #2.3 else if phase is ANOMALY:
    #2.3.1 Submit frame for model forward
    #2.3.2 Get back results and determine if normal or anomaly.