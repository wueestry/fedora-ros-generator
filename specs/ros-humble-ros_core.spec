Name:           ros-humble-ros_core
Version:        humble.0.10.0
Release:        1%{?dist}
Summary:        ROS package ros_core

License:        Apache License 2.0
URL:            http://www.ros.org/

Source0:        https://github.com/ros2-gbp/variants-release/archive/release/humble/ros_core/0.10.0-1.tar.gz#/ros2-humble-ros_core-0.10.0-source0.tar.gz



# common BRs
BuildRequires: patchelf
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

BuildRequires:  ros2-humble-ament_cmake-devel
BuildRequires:  ros2-humble-ament_package-devel

Requires:       ros2-humble-ament_cmake
Requires:       ros2-humble-ament_cmake_auto
Requires:       ros2-humble-ament_cmake_gmock
Requires:       ros2-humble-ament_cmake_gtest
Requires:       ros2-humble-ament_cmake_pytest
Requires:       ros2-humble-ament_cmake_ros
Requires:       ros2-humble-ament_index_cpp
Requires:       ros2-humble-ament_index_python
Requires:       ros2-humble-ament_lint_auto
Requires:       ros2-humble-ament_lint_common
Requires:       ros2-humble-class_loader
Requires:       ros2-humble-common_interfaces
Requires:       ros2-humble-launch
Requires:       ros2-humble-launch_ros
Requires:       ros2-humble-launch_testing
Requires:       ros2-humble-launch_testing_ament_cmake
Requires:       ros2-humble-launch_testing_ros
Requires:       ros2-humble-launch_xml
Requires:       ros2-humble-launch_yaml
Requires:       ros2-humble-pluginlib
Requires:       ros2-humble-rcl_lifecycle
Requires:       ros2-humble-rclcpp
Requires:       ros2-humble-rclcpp_action
Requires:       ros2-humble-rclcpp_lifecycle
Requires:       ros2-humble-rclpy
Requires:       ros2-humble-ros2cli_common_extensions
Requires:       ros2-humble-ros2launch
Requires:       ros2-humble-ros_environment
Requires:       ros2-humble-rosidl_default_generators
Requires:       ros2-humble-rosidl_default_runtime
Requires:       ros2-humble-sros2
Requires:       ros2-humble-sros2_cmake

Provides:  ros2-humble-ros_core = 0.10.0-1
Obsoletes: ros2-humble-ros_core < 0.10.0-1



%description
A package to aggregate the packages required to use publish /
subscribe, services, generate messages and other core ROS concepts.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros2-humble-ament_cmake-devel
Requires:       ros2-humble-ament_package-devel
Requires:       ros2-humble-ament_cmake_auto-devel
Requires:       ros2-humble-ament_cmake_gmock-devel
Requires:       ros2-humble-ament_cmake_gtest-devel
Requires:       ros2-humble-ament_cmake_pytest-devel
Requires:       ros2-humble-ament_cmake_ros-devel
Requires:       ros2-humble-ament_index_cpp-devel
Requires:       ros2-humble-ament_index_python-devel
Requires:       ros2-humble-ament_lint_auto-devel
Requires:       ros2-humble-ament_lint_common-devel
Requires:       ros2-humble-class_loader-devel
Requires:       ros2-humble-common_interfaces-devel
Requires:       ros2-humble-launch-devel
Requires:       ros2-humble-launch_ros-devel
Requires:       ros2-humble-launch_testing-devel
Requires:       ros2-humble-launch_testing_ament_cmake-devel
Requires:       ros2-humble-launch_testing_ros-devel
Requires:       ros2-humble-launch_xml-devel
Requires:       ros2-humble-launch_yaml-devel
Requires:       ros2-humble-pluginlib-devel
Requires:       ros2-humble-rcl_lifecycle-devel
Requires:       ros2-humble-rclcpp-devel
Requires:       ros2-humble-rclcpp_action-devel
Requires:       ros2-humble-rclcpp_lifecycle-devel
Requires:       ros2-humble-rclpy-devel
Requires:       ros2-humble-ros2cli_common_extensions-devel
Requires:       ros2-humble-ros2launch-devel
Requires:       ros2-humble-ros_environment-devel
Requires:       ros2-humble-rosidl_default_generators-devel
Requires:       ros2-humble-rosidl_default_runtime-devel
Requires:       ros2-humble-sros2-devel
Requires:       ros2-humble-sros2_cmake-devel

Provides: ros2-humble-ros_core-devel = 0.10.0-1
Obsoletes: ros2-humble-ros_core-devel < 0.10.0-1


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

CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \

source %{_libdir}/ros2/setup.bash

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
  --base-paths . \
  --install-base %{buildroot}/%{_libdir}/ros2/ \
  --packages-select ros_core



# remove wrong buildroot prefixes
find %{buildroot}/%{_libdir}/ros2/ -type f -exec sed -i "s:%{buildroot}::g" {} \;

rm -rf %{buildroot}/%{_libdir}/ros2/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

touch files.list
find %{buildroot}/%{_libdir}/ros2/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
# TODO: is cmake/ necessary? it stems from the yaml vendor
find %{buildroot}/%{_libdir}/ros2/{lib*/pkgconfig,include/,cmake/,ros_core/include/,share/ros_core/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
# find %{buildroot}/%{_libdir}/ros2/ -name *__rosidl_generator_py.so -type f -exec patchelf --force-rpath --add-rpath "%{_libdir}/ros2/lib" {} \;

# replace cmake python macro in shebang
for file in $(grep -rIl '^#!.*@PYTHON_EXECUTABLE@.*$' %{buildroot}) ; do
  sed -i.orig 's:^#!\s*@PYTHON_EXECUTABLE@\s*:%{__python3}:' $file
  touch -r $file.orig $file
  rm $file.orig
done


echo "This is a package automatically generated with rosfed." >> README_FEDORA
echo "See  https://github.com/morxa/rosfed for more information." >> README_FEDORA
install -m 0644 -p -D -t %{buildroot}/%{_docdir}/%{name} README_FEDORA
echo %{_docdir}/%{name} >> files.list
install -m 0644 -p -D -t %{buildroot}/%{_docdir}/%{name}-devel README_FEDORA
echo %{_docdir}/%{name}-devel >> files_devel.list

%py3_shebang_fix %{buildroot}

# Also fix .py.in files
for pyfile in $(grep -rIl '^#!.*python.*$' %{buildroot}) ; do
  %py3_shebang_fix $pyfile
done


%files -f files.list
%files devel -f files_devel.list


%changelog
* 2023-05-01 Ryan Wüest <ryan.wueest@protonmail.com> - humble.0.10.0-1
- Generate specs for humble
