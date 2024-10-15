Name:           ros2-humble-desktop
Version:        0.10.0
Release:        1%{?dist}
Summary:        ROS package desktop

License:        Apache License 2.0
URL:            http://www.ros.org/

Source0:        https://github.com/ros2-gbp/variants-release/archive/release/humble/desktop/0.10.0-1.tar.gz#/ros2-humble-desktop-0.10.0-source0.tar.gz


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

BuildRequires:  ros2-humble-ament_cmake-devel
BuildRequires:  ros2-humble-ament_package-devel

Requires:       ros2-humble-action_tutorials_cpp
Requires:       ros2-humble-action_tutorials_interfaces
Requires:       ros2-humble-action_tutorials_py
Requires:       ros2-humble-angles
Requires:       ros2-humble-composition
Requires:       ros2-humble-demo_nodes_cpp
Requires:       ros2-humble-demo_nodes_cpp_native
Requires:       ros2-humble-demo_nodes_py
Requires:       ros2-humble-depthimage_to_laserscan
Requires:       ros2-humble-dummy_map_server
Requires:       ros2-humble-dummy_robot_bringup
Requires:       ros2-humble-dummy_sensors
Requires:       ros2-humble-examples_rclcpp_minimal_action_client
Requires:       ros2-humble-examples_rclcpp_minimal_action_server
Requires:       ros2-humble-examples_rclcpp_minimal_client
Requires:       ros2-humble-examples_rclcpp_minimal_composition
Requires:       ros2-humble-examples_rclcpp_minimal_publisher
Requires:       ros2-humble-examples_rclcpp_minimal_service
Requires:       ros2-humble-examples_rclcpp_minimal_subscriber
Requires:       ros2-humble-examples_rclcpp_minimal_timer
Requires:       ros2-humble-examples_rclcpp_multithreaded_executor
Requires:       ros2-humble-examples_rclpy_executors
Requires:       ros2-humble-examples_rclpy_minimal_action_client
Requires:       ros2-humble-examples_rclpy_minimal_action_server
Requires:       ros2-humble-examples_rclpy_minimal_client
Requires:       ros2-humble-examples_rclpy_minimal_publisher
Requires:       ros2-humble-examples_rclpy_minimal_service
Requires:       ros2-humble-examples_rclpy_minimal_subscriber
Requires:       ros2-humble-image_tools
Requires:       ros2-humble-intra_process_demo
Requires:       ros2-humble-joy
Requires:       ros2-humble-lifecycle
Requires:       ros2-humble-logging_demo
Requires:       ros2-humble-pcl_conversions
Requires:       ros2-humble-pendulum_control
Requires:       ros2-humble-pendulum_msgs
Requires:       ros2-humble-quality_of_service_demo_cpp
Requires:       ros2-humble-quality_of_service_demo_py
Requires:       ros2-humble-ros_base
Requires:       ros2-humble-rqt_common_plugins
Requires:       ros2-humble-rviz2
Requires:       ros2-humble-rviz_default_plugins
Requires:       ros2-humble-teleop_twist_joy
Requires:       ros2-humble-teleop_twist_keyboard
Requires:       ros2-humble-tlsf
Requires:       ros2-humble-tlsf_cpp
Requires:       ros2-humble-topic_monitor
Requires:       ros2-humble-turtlesim

Provides:  ros2-humble-desktop = 0.10.0-1
Obsoletes: ros2-humble-desktop < 0.10.0-1



%description
A package which extends 'ros_base' and includes high level packages
like vizualization tools and demos.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ros2-humble-ament_cmake-devel
Requires:       ros2-humble-ament_package-devel
Requires:       ros2-humble-action_tutorials_cpp-devel
Requires:       ros2-humble-action_tutorials_interfaces-devel
Requires:       ros2-humble-action_tutorials_py-devel
Requires:       ros2-humble-angles-devel
Requires:       ros2-humble-composition-devel
Requires:       ros2-humble-demo_nodes_cpp-devel
Requires:       ros2-humble-demo_nodes_cpp_native-devel
Requires:       ros2-humble-demo_nodes_py-devel
Requires:       ros2-humble-depthimage_to_laserscan-devel
Requires:       ros2-humble-dummy_map_server-devel
Requires:       ros2-humble-dummy_robot_bringup-devel
Requires:       ros2-humble-dummy_sensors-devel
Requires:       ros2-humble-examples_rclcpp_minimal_action_client-devel
Requires:       ros2-humble-examples_rclcpp_minimal_action_server-devel
Requires:       ros2-humble-examples_rclcpp_minimal_client-devel
Requires:       ros2-humble-examples_rclcpp_minimal_composition-devel
Requires:       ros2-humble-examples_rclcpp_minimal_publisher-devel
Requires:       ros2-humble-examples_rclcpp_minimal_service-devel
Requires:       ros2-humble-examples_rclcpp_minimal_subscriber-devel
Requires:       ros2-humble-examples_rclcpp_minimal_timer-devel
Requires:       ros2-humble-examples_rclcpp_multithreaded_executor-devel
Requires:       ros2-humble-examples_rclpy_executors-devel
Requires:       ros2-humble-examples_rclpy_minimal_action_client-devel
Requires:       ros2-humble-examples_rclpy_minimal_action_server-devel
Requires:       ros2-humble-examples_rclpy_minimal_client-devel
Requires:       ros2-humble-examples_rclpy_minimal_publisher-devel
Requires:       ros2-humble-examples_rclpy_minimal_service-devel
Requires:       ros2-humble-examples_rclpy_minimal_subscriber-devel
Requires:       ros2-humble-image_tools-devel
Requires:       ros2-humble-intra_process_demo-devel
Requires:       ros2-humble-joy-devel
Requires:       ros2-humble-lifecycle-devel
Requires:       ros2-humble-logging_demo-devel
Requires:       ros2-humble-pcl_conversions-devel
Requires:       ros2-humble-pendulum_control-devel
Requires:       ros2-humble-pendulum_msgs-devel
Requires:       ros2-humble-quality_of_service_demo_cpp-devel
Requires:       ros2-humble-quality_of_service_demo_py-devel
Requires:       ros2-humble-ros_base-devel
Requires:       ros2-humble-rqt_common_plugins-devel
Requires:       ros2-humble-rviz2-devel
Requires:       ros2-humble-rviz_default_plugins-devel
Requires:       ros2-humble-teleop_twist_joy-devel
Requires:       ros2-humble-teleop_twist_keyboard-devel
Requires:       ros2-humble-tlsf-devel
Requires:       ros2-humble-tlsf_cpp-devel
Requires:       ros2-humble-topic_monitor-devel
Requires:       ros2-humble-turtlesim-devel

Provides: ros2-humble-desktop-devel = 0.10.0-1
Obsoletes: ros2-humble-desktop-devel < 0.10.0-1


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

source %{_libdir}/ros2-humble/setup.bash

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
  -Dgz_add_get_install_prefix_impl_OVERRIDE_INSTALL_PREFIX_ENV_VARIABLE="%{_libdir}/ros2-humble/opt/" \
  --base-paths . \
  --install-base %{buildroot}/%{_libdir}/ros2-humble/ \
  --packages-select desktop



# remove wrong buildroot prefixes
# find %{buildroot}/%{_libdir}/ros2-humble/ -type f -exec sed -i "s:%{buildroot}::g" {} \;
# we should exclude binaries from that as it might corrupt shared libraries
find %{buildroot}/%{_libdir}/ros2-humble/ -type f ! -name '*.so*' -exec sh -c 'file "{}" | grep -q text && sed -i "s:%{buildroot}::g" "{}"' \;

# # Move include directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/desktop/include ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/include/desktop ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/include/desktop
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-humble/opt/desktop/include/* %{buildroot}/%{_libdir}/ros2-humble/include/desktop/
#     rm -rd %{buildroot}/%{_libdir}/ros2-humble/opt/desktop/include
# fi

# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/desktop/extra_cmake ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/desktop/extra_cmake ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/desktop/extra_cmake
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-humble/opt/desktop/extra_cmake/* %{buildroot}/%{_libdir}/ros2-humble/desktop/extra_cmake/
#     rm -rd %{buildroot}/%{_libdir}/ros2-humble/opt/desktop/extra_cmake
# fi

# if [ -d %{buildroot}/%{_libdir}/ros2-humble/desktop/share ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/share/desktop ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/share/desktop
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-humble/desktop/share/* %{buildroot}/%{_libdir}/ros2-humble/share/desktop/
#     rm -rd %{buildroot}/%{_libdir}/ros2-humble/desktop/share
# fi

# # Move other opt path if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/desktop]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-humble/opt/desktop/* %{buildroot}/%{_libdir}/ros2-humble/
#     rm  -rd %{buildroot}/%{_libdir}/ros2-humble/opt/desktop
# fi

rm -rf %{buildroot}/%{_libdir}/ros2-humble/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# vendor pkg removal
rm -rf %{buildroot}/%{_libdir}/ros2-humble/opt/share/desktop/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# remove __pycache__
find %{buildroot} -type d -name '__pycache__' -exec rm -rf {} +
find . -name '*.pyc' -delete

touch files.list
find %{buildroot}/%{_libdir}/ros2-humble/{share,bin,etc,tools,lib64/python*,lib/python*/site-packages} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2-humble/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

# paths for vendor packages
find %{buildroot}/%{_libdir}/ros2-humble/desktop/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/desktop/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-humble/desktop/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/desktop/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/share/desktop \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/{lib*/pkgconfig,include/,cmake/,desktop/include/,share/desktop/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list
# paths for vendor packages
find %{buildroot}/%{_libdir}/ros2-humble/desktop/{lib*/pkgconfig,include/,cmake/,desktop/include/,share/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/desktop/extra_cmake \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/desktop/{lib*/pkgconfig,include/,cmake/,desktop/include/,/share/cmake,/extra_cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/share/ament_index/resource_index \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/share/colcon-core/packages/ \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/share/desktop/{hook,environment,cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2-humble/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
# find %{buildroot}/%{_libdir}/ros2-humble/ -name *__rosidl_generator_py.so -type f -exec patchelf --force-rpath --add-rpath "%{_libdir}/ros2/lib" {} \;
find %{buildroot}/%{_libdir}/ros2-humble/ -name "*.so*" -type f -exec patchelf  --shrink-rpath --allowed-rpath-prefixes %{_libdir} {} \;

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
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.5.0-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- Initial humble build
