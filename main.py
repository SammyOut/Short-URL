from flask import Flask, request, redirect, Response

app: Flask = Flask(__name__)
short_url = {}
index = 1


def base62_encode() -> str:
    base62 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    global index

    temp = []
    while index > 0:
        temp.append(base62[index % 62])
        index //= 62

    index += 1
    return ''.join(temp[::-1])


@app.route('/', methods=['POST'])
def make_short_url() -> Response:
    original_url = request.json['url']

    for short, original in short_url.items():
        if original == original_url:
            key = short
            break
    else:
        key = base62_encode()
        short_url[key] = original_url

    return Response('http://localhost/' + key, 201)


@app.route('/<key>', methods=['GET'])
def get_url(key) -> Response:
    if key not in short_url.keys():
        return Response('', 204)

    return redirect(short_url[key], 302)


if __name__ == '__main__':
    app.run('0.0.0.0', 80)
