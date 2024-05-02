# Meta Package
Name:           ros-iron-ros2cli-common-extensions
Version:        0.2.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ros2cli_common_extensions and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ros2cli_common_extensions
Requires:       ros2-iron-ros2cli_common_extensions-devel

Obsoletes: ros-iron-ros2cli-common-extensions < 0.2.2-1

%description
Meta package for ros2cli common extensions

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.2.2-1
- Update to latest release
