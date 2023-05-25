tokens = {
    "access_token": {
        "access_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..IIqIjcZLRq-IJ-GomGsjqg.XPJ-zEzfrQQ3RXU6apQsTOubNHgi1oTcnCHUzE8xrPrzahZg7ciMkmpoTBtlJA7OSiiJXlsc5dtpx-MTqCrxdoETzPodtvkm06xDLOaIxAROj4MS.QmQBEq8rIMWh7E2d8oj2rw",
        "token_type": "bearer"
    },
    "refresh_token": {
        "access_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..FQxCZvNC2Ql8ubhw7Sl01g.IK9qdTXzqztZinexeIymRE0Jka9wgU2gG5nRh2sJ24qjVQdUaClILeuNmuNdJ_Di1OH8preUcsXn7Em-LWiBHhMssIHoTG2-3iq9kY5OuEBNDKvxuA.njDxRu79rCBum_H7UPzZgw",
        "token_type": "refresh"
    }
}

aTok  = tokens["access_token"]["access_token"]
rTok  = tokens["refresh_token"]["access_token"]

import jwt

def decode_access_token(authorisation_token):

    # get public key from jwks uri

    # gives the set of jwks keys.the keys has to be passed as it is to jwt.decode() for signature verification.
    key = b'y\xf8l\xf3\xf7n\xd5y\xcf]N\xd4P;\nuy\xa2\x96\xc6\xc6~@\x00\x96\rn\x1dq]\x12\xd6'

    # get the algorithm type from the request header
    algorithm = jwt.get_unverified_header(authorisation_token).get('alg')
    print(jwt.get_unverified_header(authorisation_token))


    user_info = jwt.decode(jwt=authorisation_token,
                           key=key,
                           algorithms=algorithm)

    return user_info


print(decode_access_token(rTok))

#print(decode_access_token(rTok))