# Meta Package
Name:           ros-humble-launch-param-builder
Version:        0.1.1
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-launch_param_builder and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-launch_param_builder
Requires:       ros2-humble-launch_param_builder-devel

Obsoletes: ros-humble-launch-param-builder < 0.1.1-1

%description
Python library for loading parameters in launch files

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.1-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.1-1
- Initial humble build
