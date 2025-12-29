from IPython import get_ipython

def start_ngrok(ngrok_tokens=[], ngrok_binds=None):
    if ngrok_binds is None:
        ngrok_binds = {
            'ssh': {'port': 22, 'type': 'tcp'}
        }

    try:
        from pyngrok import ngrok, conf
    except:
        get_ipython().system('pip install -qq pyngrok')
        from pyngrok import ngrok, conf

    get_ipython().system('kill -9 "$(pgrep ngrok)" || true')

    print(f'{"*" * 10} SETUP NGROK {"*"*10}')
    ngrok_info = {}

    for token in ngrok_tokens:
        for region in ["us", "ap", "au"]:
            try:
                conf.get_default().region = region
                ngrok.set_auth_token(token)

                for name, cfg in ngrok_binds.items():
                    tunnel = ngrok.connect(cfg['port'], cfg['type'])
                    ngrok_info[name] = {
                        "public_url": tunnel.public_url,
                        "region": region
                    }

                print("> Registry success!")
                for k, v in ngrok_info.items():
                    print(f"{k}: {v['public_url']} ({v['region']})")

                return ngrok_info

            except Exception as e:
                print(f"[{region}] {e}")

    raise RuntimeError("All ngrok tokens failed")
