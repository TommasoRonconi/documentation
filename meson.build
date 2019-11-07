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

# message( 'build directory path: ' + get_option( 'mandir' ) )

#######################################################################
# Internal includes

lib_headers = []

#######################################################################
# MBH Lib

subdir( 'mbh' )

#######################################################################
# Documentation

subdir( 'doc' )

#######################################################################
# Further installation commands

# for headers ( -->/path/to/install_dir/include/... )
install_headers( lib_headers )

# for manuals ( -->/path/to/install_dir/share/man/... )
install_man()

#######################################################################

