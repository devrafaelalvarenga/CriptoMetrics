from criptometrics.extract import extract
from criptometrics.transform import transform
from criptometrics.load import load


if __name__ == "__main__":

    raw_data = extract()
    updated_data = transform(raw_data=raw_data)
    load(updated_data=updated_data)
