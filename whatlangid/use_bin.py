from os import path, mkdir

# MODEL_FILE_BIN = path.expanduser(path.join('~','fastext_model', 'lid.176.bin'))
MODEL_FILE_BIN = path.expanduser(path.join(path.dirname(__file__),'model', 'lid.176.bin'))

if __name__ == "__main__":

    import requests
    from tqdm import tqdm

    BIN_URL = "https://s3-us-west-1.amazonaws.com/fasttext-vectors/supervised_models/lid.176.bin"

    dirs = path.dirname(MODEL_FILE_BIN)
    if not path.exists(dirs):
        mkdir(dirs)
    r = requests.get(BIN_URL, stream=True)
    r_bar = '| {n_fmt}kB/{total_fmt}kB  ' '{rate_fmt}{postfix}'
    l_bar = '{desc}: {percentage:3.0f}%|'
    bar = "{bar}"
    fmt = l_bar + bar + r_bar

    with open(MODEL_FILE_BIN, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in tqdm(r.iter_content(chunk_size=1024), total=int((total_length / 1024)) + 1, unit="kB",
                          bar_format=fmt):
            if chunk:
                f.write(chunk)
                f.flush()
