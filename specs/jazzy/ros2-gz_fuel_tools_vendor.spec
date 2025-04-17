Name:           ros2-jazzy-gz_fuel_tools_vendor
Version:        0.0.6
Release:        1%{?dist}
Summary:        ROS package gz_fuel_tools_vendor

License:        Apache License 2.0
URL:            https://github.com/gazebosim/gz-fuel-tools

Source0:        https://github.com/ros2-gbp/gz_fuel_tools_vendor-release/archive/release/jazzy/gz_fuel_tools_vendor/0.0.6-1.tar.gz#/ros2-jazzy-gz_fuel_tools_vendor-0.0.6-source0.tar.gz



# common BRs
BuildRequires: patchelf
BuildRequires: coreutils
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: make
BuildRequires: patch
BuildRequires: python3-devel
BuildRequires: python-unversioned-command
BuildRequires: python3-colcon-common-extensions
BuildRequires: python3-pip
BuildRequires: python3-pydocstyle
BuildRequires: python3-pytest
BuildRequires: python3-pytest-repeat
BuildRequires: python3-pytest-rerunfailures
BuildRequires: python3-rosdep
BuildRequires: python3-setuptools
BuildRequires: python3-vcstool

# BuildRequires:  boost-devel
# BuildRequires:  console-bridge-devel
# BuildRequires:  gtest-devel
# BuildRequires:  log4cxx-devel
# BuildRequires:  python3-devel
# BuildRequires:  python3-colcon-common-extensions
# BuildRequires:  python-unversioned-command

BuildRequires:  cmake
BuildRequires:  gflags-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libcurl-devel
BuildRequires:  libyaml-devel
BuildRequires:  libzip-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  ros2-jazzy-ament_cmake_core-devel
BuildRequires:  ros2-jazzy-ament_cmake_test-devel
BuildRequires:  ros2-jazzy-ament_cmake_vendor_package-devel
BuildRequires:  ros2-jazzy-ament_package-devel
BuildRequires:  ros2-jazzy-gz_cmake_vendor-devel
BuildRequires:  ros2-jazzy-gz_common_vendor-devel
BuildRequires:  ros2-jazzy-gz_math_vendor-devel
BuildRequires:  ros2-jazzy-gz_msgs_vendor-devel
BuildRequires:  ros2-jazzy-gz_tools_vendor-devel
BuildRequires:  ros2-jazzy-gz_utils_vendor-devel

Requires:       ros2-jazzy-gz_cmake_vendor
Requires:       ros2-jazzy-gz_common_vendor
Requires:       ros2-jazzy-gz_math_vendor
Requires:       ros2-jazzy-gz_msgs_vendor
Requires:       ros2-jazzy-gz_tools_vendor
Requires:       ros2-jazzy-gz_utils_vendor

Provides:  ros2-jazzy-gz_fuel_tools_vendor = 0.0.6-1
Obsoletes: ros2-jazzy-gz_fuel_tools_vendor < 0.0.6-1



%description
Vendor package for: gz-fuel_tools9 9.1.1 Gazebo Fuel Tools: Classes
and tools for interacting with Gazebo Fuel

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake
Requires:       ros2-jazzy-ament_cmake_core-devel
Requires:       ros2-jazzy-ament_cmake_test-devel
Requires:       ros2-jazzy-ament_cmake_vendor_package-devel
Requires:       gflags-devel
Requires:       jsoncpp-devel
Requires:       libcurl-devel
Requires:       libyaml-devel
Requires:       libzip-devel
Requires:       tinyxml2-devel
Requires:       ros2-jazzy-ament_package-devel
Requires:       ros2-jazzy-gz_cmake_vendor-devel
Requires:       ros2-jazzy-gz_common_vendor-devel
Requires:       ros2-jazzy-gz_math_vendor-devel
Requires:       ros2-jazzy-gz_msgs_vendor-devel
Requires:       ros2-jazzy-gz_tools_vendor-devel
Requires:       ros2-jazzy-gz_utils_vendor-devel

Provides: ros2-jazzy-gz_fuel_tools_vendor-devel = 0.0.6-1
Obsoletes: ros2-jazzy-gz_fuel_tools_vendor-devel < 0.0.6-1


%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.



%prep

%setup -c -T
tar --strip-components=1 -xf %{SOURCE0}

%build
# nothing to do here


%install

PYTHONUNBUFFERED=1 ; export PYTHONUNBUFFERED
GZ_BUILD_FROM_SURCE=1; export GZ_BUILD_FROM_SOURCE
export GZ_VERSION=harmonic;

CFLAGS=" -Wno-error ${CFLAGS:-%optflags} -Wno-error -w -Wno-error=int-conversion" ; export CFLAGS ; \
CXXFLAGS=" -Wno-error ${CXXFLAGS:-%optflags} -Wno-error -w -Wno-error=int-conversion" ; export CXXFLAGS ; \
FFLAGS=" -Wno-error ${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}} -w -Wno-error=int-conversion" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}} -w -Wno-error=int-conversion" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \

source %{_libdir}/ros2-jazzy/setup.bash

# substitute shebang before install block because we run the local catkin script
%py3_shebang_fix .

# DESTDIR=%{buildroot} ; export DESTDIR

colcon \
  build \
  --merge-install \
  --cmake-args -DPYTHON_EXECUTABLE="/usr/bin/python" \
  -DTHIRDPARTY_Asio=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
  -DCMAKE_C_FLAGS="$CFLAGS" \
  -DCMAKE_LD_FLAGS="$LDFLAGS" \
  -DBUILD_TESTING=OFF \
  -Dgz_add_get_install_prefix_impl_OVERRIDE_INSTALL_PREFIX_ENV_VARIABLE="%{_libdir}/ros2-jazzy/opt/" \
  --base-paths . \
  --install-base %{buildroot}/%{_libdir}/ros2-jazzy/ \
  --packages-select gz_fuel_tools_vendor



# remove wrong buildroot prefixes
# find %{buildroot}/%{_libdir}/ros2-jazzy/ -type f -exec sed -i "s:%{buildroot}::g" {} \;
# we should exclude binaries from that as it might corrupt shared libraries
find %{buildroot}/%{_libdir}/ros2-jazzy/ -type f ! -name '*.so*' -exec sh -c 'file "{}" | grep -q text && sed -i "s:%{buildroot}::g" "{}"' \;

# # Move include directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/gz_fuel_tools_vendor/include ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/include/gz_fuel_tools_vendor ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/include/gz_fuel_tools_vendor
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/opt/gz_fuel_tools_vendor/include/* %{buildroot}/%{_libdir}/ros2-jazzy/include/gz_fuel_tools_vendor/
#     rm -rd %{buildroot}/%{_libdir}/ros2-jazzy/opt/gz_fuel_tools_vendor/include
# fi

# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/gz_fuel_tools_vendor/extra_cmake ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/gz_fuel_tools_vendor/extra_cmake ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/gz_fuel_tools_vendor/extra_cmake
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/opt/gz_fuel_tools_vendor/extra_cmake/* %{buildroot}/%{_libdir}/ros2-jazzy/gz_fuel_tools_vendor/extra_cmake/
#     rm -rd %{buildroot}/%{_libdir}/ros2-jazzy/opt/gz_fuel_tools_vendor/extra_cmake
# fi

# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/gz_fuel_tools_vendor/share ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/share/gz_fuel_tools_vendor ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/share/gz_fuel_tools_vendor
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/gz_fuel_tools_vendor/share/* %{buildroot}/%{_libdir}/ros2-jazzy/share/gz_fuel_tools_vendor/
#     rm -rd %{buildroot}/%{_libdir}/ros2-jazzy/gz_fuel_tools_vendor/share
# fi

# # Move other opt path if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/gz_fuel_tools_vendor]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/opt/gz_fuel_tools_vendor/* %{buildroot}/%{_libdir}/ros2-jazzy/
#     rm  -rd %{buildroot}/%{_libdir}/ros2-jazzy/opt/gz_fuel_tools_vendor
# fi

rm -rf %{buildroot}/%{_libdir}/ros2-jazzy/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# vendor pkg removal
rm -rf %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/gz_fuel_tools_vendor/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# remove __pycache__
find %{buildroot} -type d -name '__pycache__' -exec rm -rf {} +
find . -name '*.pyc' -delete

touch files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/{share,bin,etc,tools,lib64/python*,lib/python*/site-packages,lib/python*/dist-packages} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

# paths for vendor packages
find %{buildroot}/%{_libdir}/ros2-jazzy/gz_fuel_tools_vendor/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/gz_fuel_tools_vendor/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/gz_fuel_tools_vendor/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/gz_fuel_tools_vendor/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/gz_fuel_tools_vendor \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/{lib*/pkgconfig,include/,cmake/,gz_fuel_tools_vendor/include/,share/gz_fuel_tools_vendor/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list
# paths for vendor packages
find %{buildroot}/%{_libdir}/ros2-jazzy/gz_fuel_tools_vendor/{lib*/pkgconfig,include/,cmake/,extra_cmake/,gz_fuel_tools_vendor/include/,share/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/gz_fuel_tools_vendor/extra_cmake \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/gz_fuel_tools_vendor/{lib*/pkgconfig,include/,cmake/,gz_fuel_tools_vendor/include/,/share/cmake,/extra_cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/ament_index/resource_index \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/colcon-core/packages/ \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/gz_fuel_tools_vendor/{hook,environment,cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2-jazzy/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
# find %{buildroot}/%{_libdir}/ros2-jazzy/ -name *__rosidl_generator_py.so -type f -exec patchelf --force-rpath --add-rpath "%{_libdir}/ros2/lib" {} \;
find %{buildroot}/%{_libdir}/ros2-jazzy/ -name "*.so*" -type f -exec patchelf  --shrink-rpath --allowed-rpath-prefixes %{_libdir} {} \;

# replace cmake python macro in shebang
for file in $(grep -rIl '^#!.*@PYTHON_EXECUTABLE@.*$' %{buildroot}) ; do
  sed -i.orig 's:^#!\s*@PYTHON_EXECUTABLE@\s*:%{__python3}:' $file
  touch -r $file.orig $file
  rm $file.orig
done


echo "This is a package automatically generated with rosfed." >> README_FEDORA
echo "See  https://github.com/TarikViehmann/rosfed for more information." >> README_FEDORA
install -m 0644 -p -D -t %{buildroot}/%{_docdir}/%{name} README_FEDORA
echo %{_docdir}/%{name} >> files.list
install -m 0644 -p -D -t %{buildroot}/%{_docdir}/%{name}-devel README_FEDORA
echo %{_docdir}/%{name}-devel >> files_devel.list

%py3_shebang_fix %{buildroot}

# Also fix .py.in files
for pyfile in $(grep -rIl '^#!.*python.*$' %{buildroot}) ; do
  %py3_shebang_fix $pyfile
done

sort files.list | uniq > files.list.tmp && mv files.list.tmp files.list
sort files_devel.list | uniq > files_devel.list.tmp && mv files_devel.list.tmp files_devel.list

%files -f files.list
%files devel -f files_devel.list


%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.6-1
- Update to latest release
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.5-1
- Update to latest release
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.4-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.3-1
- Update to latest release
