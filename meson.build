#######################################################################
# Global project info

project( 'master',
         'cpp',
         default_options : [ 'cpp_std=c++17',
                             'buildtype=debugoptimized',
                             'prefix=' + meson.source_root() + '/install',
                             'libdir=lib' ],
         version : '0.1.0',
         license : 'SISSA' )

root = meson.source_root()

#######################################################################
# External dependencies

#######################################################################
# Internal includes

lib_headers = []

#######################################################################
# MBH Lib

subdir( 'mbh' )

#######################################################################
# Further installation commands

install_headers( lib_headers )

#######################################################################
#

#######################################################################
#
