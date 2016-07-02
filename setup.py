from setuptools import setup

setup(
    name="electrum-vcn-server",
    version="0.9",
    scripts=['run_electrum_vcn_server','electrum-vcn-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumvcnserver':'src'
        },
    py_modules=[
        'electrumvcnserver.__init__',
        'electrumvcnserver.utils',
        'electrumvcnserver.storage',
        'electrumvcnserver.deserialize',
        'electrumvcnserver.networks',
        'electrumvcnserver.blockchain_processor',
        'electrumvcnserver.server_processor',
        'electrumvcnserver.processor',
        'electrumvcnserver.version',
        'electrumvcnserver.ircthread',
        'electrumvcnserver.stratum_tcp',
        'electrumvcnserver.stratum_http'
    ],
    description="Namecoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/spesmilo/electrum-server/",
    long_description="""Server for the Electrum-VCN Lightweight Namecoin Wallet"""
)


