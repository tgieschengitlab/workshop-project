import os
from notes import note

aws_key_id = "AKIAIOSF0DNN7EXAMPLE"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    note.run(host='0.0.0.0', port=port, debug=True)
