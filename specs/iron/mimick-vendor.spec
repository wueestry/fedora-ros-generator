# Meta Package
Name:           ros-iron-mimick-vendor
Version:        0.3.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/Snaipe/Mimick
Summary:        Meta package for ros2-iron-mimick_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-mimick_vendor
Requires:       ros2-iron-mimick_vendor-devel

Obsoletes: ros-iron-mimick-vendor < 0.3.2-1

%description
Wrapper around mimick, it provides an ExternalProject build of mimick.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.3.2-1
- Update to latest release
