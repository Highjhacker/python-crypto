from crypto.constants import TRANSACTION_MULTI_SIGNATURE_REGISTRATION
from crypto.transactions.builder.multi_signature_registration import MultiSignatureRegistration


def test_multi_signature_registration_transaction():
    """Test if a second signature registration transaction gets built
    """
    publicKeys = [
        '0205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b896',
        '03df0a1eb42d99b5de395cead145ba1ec2ea837be308c7ce3a4e8018b7efc7fdb8',
        '03860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17f',
    ]
    transaction = MultiSignatureRegistration(2, 255, publicKeys)
    transaction.sign('secret')
    transaction.second_sign('second secret')
    transaction_dict = transaction.to_dict()
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_MULTI_SIGNATURE_REGISTRATION
    transaction.verify()  # if no exception is raised, it means the transaction is valid
