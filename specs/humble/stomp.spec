# Meta Package
Name:           ros-humble-stomp
Version:        0.1.2
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://wiki.ros.org/stomp
Summary:        Meta package for ros2-humble-stomp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-stomp
Requires:       ros2-humble-stomp-devel

Obsoletes: ros-humble-stomp < 0.1.2-1

%description
This package provides the STOMP (Stochastic Trajectory Optimization
for Motion Planning) algorithm that can be used for robot motion
planning tasks or other similar optimization tasks

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.2-1
- Update to latest release
