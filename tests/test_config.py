import config


def test_model_name():
    assert config.MODEL_NAME != ""


def test_embedding_model():
    assert config.EMBEDDING_MODEL != ""


def test_top_k_results():
    assert config.TOP_K_RESULTS > 0


def test_report_file():
    assert config.REPORT_FILE.endswith(".md")


def test_input_file():
    assert config.INPUT_FILE.endswith((".json", ".jsonl"))