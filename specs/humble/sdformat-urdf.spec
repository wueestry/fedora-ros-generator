# Meta Package
Name:           ros-humble-sdformat-urdf
Version:        1.0.1
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-sdformat_urdf and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-sdformat_urdf
Requires:       ros2-humble-sdformat_urdf-devel

Obsoletes: ros-humble-sdformat-urdf < 1.0.1-1

%description
URDF plugin to parse SDFormat XML into URDF C++ DOM objects.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.1-1
- Update to latest release
