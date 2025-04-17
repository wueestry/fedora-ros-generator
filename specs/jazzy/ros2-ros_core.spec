Name:           ros2-jazzy-ros_core
Version:        0.11.0
Release:        1%{?dist}
Summary:        ROS package ros_core

License:        Apache License 2.0
URL:            http://www.ros.org/

Source0:        https://github.com/ros2-gbp/variants-release/archive/release/jazzy/ros_core/0.11.0-1.tar.gz#/ros2-jazzy-ros_core-0.11.0-source0.tar.gz


BuildArch: noarch

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

BuildRequires:  ros2-jazzy-ament_cmake-devel
BuildRequires:  ros2-jazzy-ament_package-devel

Requires:       ros2-jazzy-ament_cmake
Requires:       ros2-jazzy-ament_cmake_auto
Requires:       ros2-jazzy-ament_cmake_gmock
Requires:       ros2-jazzy-ament_cmake_gtest
Requires:       ros2-jazzy-ament_cmake_pytest
Requires:       ros2-jazzy-ament_cmake_ros
Requires:       ros2-jazzy-ament_index_cpp
Requires:       ros2-jazzy-ament_index_python
Requires:       ros2-jazzy-ament_lint_auto
Requires:       ros2-jazzy-ament_lint_common
Requires:       ros2-jazzy-class_loader
Requires:       ros2-jazzy-common_interfaces
Requires:       ros2-jazzy-launch
Requires:       ros2-jazzy-launch_ros
Requires:       ros2-jazzy-launch_testing
Requires:       ros2-jazzy-launch_testing_ament_cmake
Requires:       ros2-jazzy-launch_testing_ros
Requires:       ros2-jazzy-launch_xml
Requires:       ros2-jazzy-launch_yaml
Requires:       ros2-jazzy-pluginlib
Requires:       ros2-jazzy-rcl_lifecycle
Requires:       ros2-jazzy-rclcpp
Requires:       ros2-jazzy-rclcpp_action
Requires:       ros2-jazzy-rclcpp_lifecycle
Requires:       ros2-jazzy-rclpy
Requires:       ros2-jazzy-ros2cli_common_extensions
Requires:       ros2-jazzy-ros2launch
Requires:       ros2-jazzy-ros_environment
Requires:       ros2-jazzy-rosidl_default_generators
Requires:       ros2-jazzy-rosidl_default_runtime
Requires:       ros2-jazzy-sros2
Requires:       ros2-jazzy-sros2_cmake

Provides:  ros2-jazzy-ros_core = 0.11.0-1
Obsoletes: ros2-jazzy-ros_core < 0.11.0-1



%description
A package to aggregate the packages required to use publish /
subscribe, services, generate messages and other core ROS concepts.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ros2-jazzy-ament_cmake-devel
Requires:       ros2-jazzy-ament_package-devel
Requires:       ros2-jazzy-ament_cmake_auto-devel
Requires:       ros2-jazzy-ament_cmake_gmock-devel
Requires:       ros2-jazzy-ament_cmake_gtest-devel
Requires:       ros2-jazzy-ament_cmake_pytest-devel
Requires:       ros2-jazzy-ament_cmake_ros-devel
Requires:       ros2-jazzy-ament_index_cpp-devel
Requires:       ros2-jazzy-ament_index_python-devel
Requires:       ros2-jazzy-ament_lint_auto-devel
Requires:       ros2-jazzy-ament_lint_common-devel
Requires:       ros2-jazzy-class_loader-devel
Requires:       ros2-jazzy-common_interfaces-devel
Requires:       ros2-jazzy-launch-devel
Requires:       ros2-jazzy-launch_ros-devel
Requires:       ros2-jazzy-launch_testing-devel
Requires:       ros2-jazzy-launch_testing_ament_cmake-devel
Requires:       ros2-jazzy-launch_testing_ros-devel
Requires:       ros2-jazzy-launch_xml-devel
Requires:       ros2-jazzy-launch_yaml-devel
Requires:       ros2-jazzy-pluginlib-devel
Requires:       ros2-jazzy-rcl_lifecycle-devel
Requires:       ros2-jazzy-rclcpp-devel
Requires:       ros2-jazzy-rclcpp_action-devel
Requires:       ros2-jazzy-rclcpp_lifecycle-devel
Requires:       ros2-jazzy-rclpy-devel
Requires:       ros2-jazzy-ros2cli_common_extensions-devel
Requires:       ros2-jazzy-ros2launch-devel
Requires:       ros2-jazzy-ros_environment-devel
Requires:       ros2-jazzy-rosidl_default_generators-devel
Requires:       ros2-jazzy-rosidl_default_runtime-devel
Requires:       ros2-jazzy-sros2-devel
Requires:       ros2-jazzy-sros2_cmake-devel

Provides: ros2-jazzy-ros_core-devel = 0.11.0-1
Obsoletes: ros2-jazzy-ros_core-devel < 0.11.0-1


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
  --packages-select ros_core



# remove wrong buildroot prefixes
# find %{buildroot}/%{_libdir}/ros2-jazzy/ -type f -exec sed -i "s:%{buildroot}::g" {} \;
# we should exclude binaries from that as it might corrupt shared libraries
find %{buildroot}/%{_libdir}/ros2-jazzy/ -type f ! -name '*.so*' -exec sh -c 'file "{}" | grep -q text && sed -i "s:%{buildroot}::g" "{}"' \;

# # Move include directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/ros_core/include ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/include/ros_core ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/include/ros_core
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/opt/ros_core/include/* %{buildroot}/%{_libdir}/ros2-jazzy/include/ros_core/
#     rm -rd %{buildroot}/%{_libdir}/ros2-jazzy/opt/ros_core/include
# fi

# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/ros_core/extra_cmake ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/ros_core/extra_cmake ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/ros_core/extra_cmake
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/opt/ros_core/extra_cmake/* %{buildroot}/%{_libdir}/ros2-jazzy/ros_core/extra_cmake/
#     rm -rd %{buildroot}/%{_libdir}/ros2-jazzy/opt/ros_core/extra_cmake
# fi

# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/ros_core/share ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/share/ros_core ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/share/ros_core
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/ros_core/share/* %{buildroot}/%{_libdir}/ros2-jazzy/share/ros_core/
#     rm -rd %{buildroot}/%{_libdir}/ros2-jazzy/ros_core/share
# fi

# # Move other opt path if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/ros_core]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/opt/ros_core/* %{buildroot}/%{_libdir}/ros2-jazzy/
#     rm  -rd %{buildroot}/%{_libdir}/ros2-jazzy/opt/ros_core
# fi

rm -rf %{buildroot}/%{_libdir}/ros2-jazzy/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# vendor pkg removal
rm -rf %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/ros_core/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

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
find %{buildroot}/%{_libdir}/ros2-jazzy/ros_core/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/ros_core/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/ros_core/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/ros_core/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/ros_core \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/{lib*/pkgconfig,include/,cmake/,ros_core/include/,share/ros_core/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list
# paths for vendor packages
find %{buildroot}/%{_libdir}/ros2-jazzy/ros_core/{lib*/pkgconfig,include/,cmake/,extra_cmake/,ros_core/include/,share/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/ros_core/extra_cmake \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/ros_core/{lib*/pkgconfig,include/,cmake/,ros_core/include/,/share/cmake,/extra_cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/ament_index/resource_index \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/colcon-core/packages/ \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/ros_core/{hook,environment,cmake} \
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
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.11.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.10.0-1
- Update to latest release
